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
        out = self.forward(obs)
        coin = random.random()
        if coin < epsilon:
            return random.randint(0,1)
        else : 
            return out.argmax().item()  # out의 가장 큰 값(액션밸류 가장 큰 값) 출력



############################### 학습 진행 함수
def train(q, q_target, memory, optimizer):
    for i in range(10):
        s,a,r,s_prime,done_mask = memory.sample(batch_size)

        q_out = q(s)
        q_a = q_out.gather(1,a)
        max_q_prime = q_target(s_prime).max(1)[0].unsqueeze(1)
        target = r + gamma * max_q_prime * done_mask
        loss = F.smooth_l1_loss(q_a, target)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()



###############################
def main():
    env = gym.make('CartPole-v1')
    q = Qnet()
    q_target = Qnet()
    q_target.load_state_dict(q.state_dict())
    memory = ReplayBuffer()

    print_interval = 20
    score = 0.0  
    optimizer = optim.Adam(q.parameters(), lr=learning_rate)

    for n_epi in range(10000):
        epsilon = max(0.01, 0.08 - 0.01*(n_epi/200)) #Linear annealing from 8% to 1%
        s, _ = env.reset()
        done = False

        while not done:
            a = q.sample_action(torch.from_numpy(s).float(), epsilon)      
            s_prime, r, done, truncated, info = env.step(a)
            done_mask = 0.0 if done else 1.0
            memory.put((s,a,r/100.0,s_prime, done_mask))
            s = s_prime

            score += r
            if done:
                break
            
        if memory.size()>2000:
            train(q, q_target, memory, optimizer)

        if n_epi%print_interval==0 and n_epi!=0:
            q_target.load_state_dict(q.state_dict())
            print("n_episode :{}, score : {:.1f}, n_buffer : {}, eps : {:.1f}%".format(
                                                            n_epi, score/print_interval, memory.size(), epsilon*100))
            score = 0.0
    env.close()

if __name__ == '__main__':
    main()