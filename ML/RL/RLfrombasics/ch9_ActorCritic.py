import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

################### Hyperparameters
learning_rate = 0.0002      # 스텝사이즈
gamma         = 0.98        # 감쇠인자
n_rollout     = 10          # 몇 틱의 데이터를 쌓아서 업데이트 할지
# 액터-크리틱은 리턴이 아니라 TD 타깃을 사용 -> 한틱의 데이터로 바로 업데이트 가능



################### 액터 크리틱 클래스
class ActorCritic(nn.Module):
    def __init__(self):
        super(ActorCritic, self).__init__()
        self.data = []
        
        self.fc1 = nn.Linear(4,256)
        self.fc_pi = nn.Linear(256,2)   # 정책 네트워크 - 2개의 액션값에 대한 확률값 리턴
        self.fc_v = nn.Linear(256,1)    # 밸류 네트워크 - 입력의 밸류값 리턴
        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)
        
    def pi(self, x, softmax_dim = 0):   # 정책 네트워크
        x = F.relu(self.fc1(x))
        x = self.fc_pi(x)
        prob = F.softmax(x, dim=softmax_dim)
        return prob
    
    def v(self, x):                     # 밸류 네트워크
        x = F.relu(self.fc1(x))
        v = self.fc_v(x)
        return v
    
    def put_data(self, transition):
        self.data.append(transition)
        
    def make_batch(self):               # 배치 생성
        s_lst, a_lst, r_lst, s_prime_lst, done_lst = [], [], [], [], []
        for transition in self.data:
            s,a,r,s_prime,done = transition
            s_lst.append(s)
            a_lst.append([a])
            r_lst.append([r/100.0])
            s_prime_lst.append(s_prime)
            done_mask = 0.0 if done else 1.0
            done_lst.append([done_mask])
        
        s_batch, a_batch, r_batch, s_prime_batch, done_batch = torch.tensor(s_lst, dtype=torch.float), torch.tensor(a_lst), \
                                                            torch.tensor(r_lst, dtype=torch.float), torch.tensor(s_prime_lst, dtype=torch.float), \
                                                            torch.tensor(done_lst, dtype=torch.float)
        self.data = []          # 초기화
        return s_batch, a_batch, r_batch, s_prime_batch, done_batch
    

    # 네트워크 학습하는 함수
    def train_net(self):
        s, a, r, s_prime, done = self.make_batch()
        # delta 계산
        td_target = r + gamma * self.v(s_prime) * done
        delta     = td_target - self.v(s)
        

        pi = self.pi(s, softmax_dim=1)
        pi_a = pi.gather(1,a)       # q_out에서 a에 해당하는 인덱스 반환. 즉, 실제 행동한 액션의 인덱스 반환 (32*1)
        # 정책 네트워크의 손실 함수(maximize'-') + 밸류 네트워크 손실 함수(minimize'+') - 한꺼번에 업데이트
        # detach - 함수취급을 위해 (정책과 현재 밸류만 업데이트 위해)
        loss = -torch.log(pi_a) * delta.detach() + F.smooth_l1_loss(self.v(s), td_target.detach())

        self.optimizer.zero_grad()
        loss.mean().backward()
        self.optimizer.step()         



################### 메인 함수
def main():  
    env = gym.make('CartPole-v1')
    model = ActorCritic()       # 액터 크리틱
    print_interval = 20
    score = 0.0

    for n_epi in range(1000):   # 에피소드 1000개
        done = False
        s, _ = env.reset()      # 초기상태 s
        
        while not done:         # 한 에피소드
            for t in range(n_rollout):                           # n개의 틱
                prob = model.pi(torch.from_numpy(s).float())     # 상태s의 2개의 액션에 대한 확률값 (정책확률)
                m = Categorical(prob)                            # 확률 변수 prob에 의해 주어진 확률들로 이루어진 범주형 분포 객체 m을 생성
                a = m.sample().item()                            # 확률 분포 m에 기반하여  m에서 카테고리 하나 랜덤하게 추출 -> 변수 a에 할당(액션)
                s_prime, r, done, truncated, info = env.step(a)  
                model.put_data((s,a,r,s_prime,done))             
                
                s = s_prime
                score += r
                
                if done:
                    break                     
            
            model.train_net()                                     # n개의 틱이 끝날때마다 파라미터 업데이트 
            
        if n_epi%print_interval==0 and n_epi!=0:                  # 에피소드 20개마다 출력
            print("# of episode :{}, avg score : {:.1f}".format(n_epi, score/print_interval))
            score = 0.0
    env.close()

if __name__ == '__main__':
    main()