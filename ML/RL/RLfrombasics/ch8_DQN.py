import gym
# 리플레이 버퍼를 구현할 때 사용
import collections
import random

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


############################### Hyperparameter 정의
learning_rate = 0.0005
gamma         = 0.98   # 감쇠인자
buffer_limit  = 50000
batch_size    = 32



############################### 리플레이 버퍼 클래스
class ReplayBuffer():
    def __init__(self):             # 버퍼 생성
        self.buffer = collections.deque(maxlen=buffer_limit)
    
    def put(self, transition):      # 데이터를 버퍼에 넣어주는 함수
        self.buffer.append(transition)
    
    def sample(self, n):            # 버에서 랜덤하게 32개의 데이터를 뽑아 미니배치를 구성해주는 함수
        mini_batch = random.sample(self.buffer, n)   # self.buffer에서 중복없이 n개 요소 선택
        s_lst, a_lst, r_lst, s_prime_lst, done_mask_lst = [], [], [], [], []    
        # done_mask : 종료(0), 종료x(1)- q(s,a)에 곱하여 밸류표현(종료 상태의 밸류 = 0)
        
        for transition in mini_batch:
            s, a, r, s_prime, done_mask = transition
            s_lst.append(s)
            a_lst.append([a])
            r_lst.append([r])
            s_prime_lst.append(s_prime)
            done_mask_lst.append([done_mask])

        # pytorch의 텐서로 변환
        return torch.tensor(s_lst, dtype=torch.float), torch.tensor(a_lst), \
            torch.tensor(r_lst), torch.tensor(s_prime_lst, dtype=torch.float), \
            torch.tensor(done_mask_lst)
    
    def size(self):           
        return len(self.buffer)



############################### 에이전트(Q밸류 네트워크 클래스) : 정책 따라 움직임
class Qnet(nn.Module):      # nn.Module : 뉴럴넷을 만들 때 뼈대가 되는 파이토치 라이브러리의 클래스
    def __init__(self):     #
        super(Qnet, self).__init__()
        self.fc1 = nn.Linear(4, 128)    # 인풋벡터(카트의 위치정보, 카트의 속도정보, 막대의 각도, 막대의 각속도)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 2)    # 모든 액션에 대해 각 액션의 밸류인 Q(s,a)의 값을 리턴
                                        # 액션이 2개이므로 아웃풋의 차원은 2

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)                 # 마지막엔 양수만 리턴하는 Relu (X)
                                        # 이유 : 맨 마지막 아웃풋은 Q밸류이기 때문에 어느 값이든 가능
        return x
    
    def sample_action(self, obs, epsilon):
        # eps-greedy로 액션을 선택
        out  = self.forward(obs)
        coin = random.random()
        if coin < epsilon:
            return random.randint(0,1)
        else : 
            return out.argmax().item()  # out의 가장 큰 값(액션밸류 가장 큰 값) 출력



############################### 학습 진행 함수
def train(q, q_target, memory, optimizer):
    for i in range(10): # 10개의 미니배치(320개 데이터)를 뽑아 총 10번 파라미터 업데이트
        s,a,r,s_prime,done_mask = memory.sample(batch_size)  # 리플버퍼에서 상관성 x 32개 데이터 뽑아 하나의 배치 생성
        # s와 s_prime:(32*4), a와 done_mask:(32*1)

        q_out       = q(s)            # 32*4 input -> 32*2 output (액션밸류)
        q_a         = q_out.gather(1,a) # q_out에서 a에 해당하는 인덱스 반환. 즉, 실제 행동한 액션의 인덱스 반환 (32*1)
        max_q_prime = q_target(s_prime).max(1)[0].unsqueeze(1)  # for TD타깃. 액션밸류가 가장 큰 액션밸류 값 반환 (32*1)
        # max(1): 각 행에서 최댓값과 그 인덱스 반환. max(1)[0]: 각 행의 최댓값 텐서 값만 반환
        # unsqueeze(1): 1번째 차원(열 방향)을 확장하여 텐서 구조 변환
        target = r + gamma * max_q_prime * done_mask    # TD 타깃값 (32*1)
        loss   = F.smooth_l1_loss(q_a, target)          # 손실값 계산 smooth_l1_loss(추정치, 타깃값)
        
        optimizer.zero_grad()   # 파라미터 초기화
        loss.backward()         # 역전파(그라디언트 계산)
        optimizer.step()        # 파라미터 업데이트



############################### 메인 함수
def main():
    env      = gym.make('CartPole-v1')
    # 행동정책과 타깃정책 분리
    q        = Qnet()  # 행동정책
    q_target = Qnet()  # 타깃정책
    q_target.load_state_dict(q.state_dict())  # 초기에 서로의 파라미터 동일하도록
    memory   = ReplayBuffer()

    print_interval = 20
    score          = 0.0
    optimizer      = optim.Adam(q.parameters(), lr=learning_rate) # q 네트워크만 업데이트 (타깃정책은 업데이트 X)

    for n_epi in range(10000):  # 10000개 에피소드 진행
        epsilon   = max(0.01, 0.08 - 0.01*(n_epi/200)) # eps-greedy 행동정책 위해
        s, _      = env.reset() # 환경 초기화 후 초기 상태 반환 (_는 무시하기 위해 사용)
        done      = False       # 종료상태가 되면 True

        while not done: # 종료 상태 될 때까지 진행. 즉, 한 에피소드 진행
            a = q.sample_action(torch.from_numpy(s).float(), epsilon) # s의 실제 행동 a 반환     
            s_prime, r, done, truncated, info = env.step(a)
            done_mask = 0.0 if done else 1.0
            memory.put((s,a,r/100.0,s_prime, done_mask))             # 보상이 커서 스케일 조절하기 위해 100으로 나눔
            s = s_prime

            score += r      # 한 에피소드의 보상의 합
            if done:
                break
        
        # 에피소드가 끝나고 학습 진행 
        # 리플레이버퍼에 데이터 충분히 쌓지 않고 학습 진행(파라미터 업데이트)시 학습이 초기 데이터에 치우칠 수 있음
        # -> 2000개 이상 데이터가 쌓였을 때부터 학습 진행
        if memory.size()>2000:  
            train(q, q_target, memory, optimizer)


        if n_epi%print_interval==0 and n_epi!=0:        # 에피소드가 20개 끝날 때마다
            q_target.load_state_dict(q.state_dict())    # q_target 네트워크에 q 네트워크 파라미터 복사
            print("n_episode :{}, score : {:.1f}, n_buffer : {}, eps : {:.1f}%".format(
                                                            n_epi, score/print_interval, memory.size(), epsilon*100))
            score = 0.0
    env.close()

if __name__ == '__main__':
    main()