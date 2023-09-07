import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

################### Hyperparameters
learning_rate = 0.0002  # 스텝사이즈
gamma         = 0.98    # 감쇠인자



################### 정책 네트워크 클래스
class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.data = []
        
        self.fc1 = nn.Linear(4, 128)
        self.fc2 = nn.Linear(128, 2)    # 2개의 액션값에 대한 확률값 리턴
        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        # 소프트맥스 함수: 각 원소를 [0, 1] 범위로 변환, 모든 원소의 합은 1 -> 2개의 액션에 대한 확률값
        x = F.softmax(self.fc2(x), dim=0)
        return x
    
    def put_data(self, item):
        self.data.append(item)
    
    # 네트워크 학습하는 함수
    def train_net(self):
        R = 0
        self.optimizer.zero_grad()          # 파라미터 초기화
        for r, prob in self.data[::-1]:     # 한 에피소드의 r, prob
            R = r + gamma * R               # 리턴 계산
            loss = -torch.log(prob) * R     # J(θ) 최대화하기 위해 - 붙임
            loss.backward()                 # -J(θ) 그라디언트 계산
        self.optimizer.step()               # 파라미터 업데이트: θ<-θ+learning_rate*(J(θ)gradient)
        self.data = []                      # 에피소드 비우기 



################### 메인 함수
def main():
    env = gym.make('CartPole-v1')
    pi = Policy()           # 정책 네트워크
    score = 0.0             
    print_interval = 20
    
    for n_epi in range(1000):  # 에피소드 1000개
        s, _ = env.reset()      # 초기상태 s
        done = False
        
        while not done:
            prob = pi(torch.from_numpy(s).float())  # 상태s의 2개의 액션에 대한 확률값 (정책확률)
            m = Categorical(prob)   # 확률 변수 prob에 의해 주어진 확률들로 이루어진 범주형 분포 객체 m을 생성
            # 상태 s에서의 액션 a 뽑기
            a = m.sample()          # 확률 분포 m에 기반하여  m에서 카테고리 하나 랜덤하게 추출 -> 변수 a에 할당(액션)
            s_prime, r, done, truncated, info = env.step(a.item()) # a.item(): 하나의 값만 추출
            pi.put_data((r,prob[a]))    # prob[a]: 상태 s에서 a를 선택할 확률
            s = s_prime
            score += r                 
            
        pi.train_net()  # 에피소드 끝날때마다 파라미터 업데이트
        
        if n_epi%print_interval==0 and n_epi!=0:        # 에피소드 20개마다 출력
            print("# of episode :{}, avg score : {}".format(n_epi, score/print_interval))
            score = 0.0 # 에피소드 20개 리턴 총합 (감쇠인자가 1일 때)
    env.close()
    
if __name__ == '__main__':
    main()