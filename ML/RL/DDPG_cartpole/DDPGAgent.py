import torch
from Actor import Actor
from Critic import Critic
import copy
from Noise import OU_noise
from collections import deque
import random
from Utils import convertToTensorInput
import numpy as np

########## 하이퍼파라미터

batch_size      = 128   # 배치 사이즈
mem_maxlen      = 5000  # 리플레이버퍼 사이즈
discount_factor = 0.99  # gamma (감쇠인자)

actor_lr  = 1e-4        # 액터(정책함수) 학습률
critic_lr = 5e-4        # 크리틱(액션가치함수) 학습률

tau = 1e-3              # soft target network update 파라미터



########## DDPG Agent
class Agent():
    def __init__(self, state_size, action_size, train_mode_, load_model_):
        self.train_mode = train_mode_
        self.load_model = load_model_

        self.state_size  = state_size
        self.action_size = action_size

        self.actor  = Actor(self.state_size, self.action_size)
        self.critic = Critic(self.state_size, self.action_size)

        self.target_actor  = copy.deepcopy(self.actor)  # deepcopy: 원본 객체에 영향 X
        self.target_critic = copy.deepcopy(self.critic)

        self.OU     = OU_noise(action_size)
        self.memory = deque(maxlen=mem_maxlen)

        self.actor_optimizer  = torch.optim.Adam(self.actor.parameters(), lr=actor_lr)
        self.critic_optimizer = torch.optim.Adam(self.critic.parameters(), lr=critic_lr)


    ##### 액션 선택 함수
    def get_action(self, state):
        # 각 액션의 확률 (정책함수)
        state_vector = np.array([float(x[1:]) if x[0]=='[' else float(x[:-1]) for x in str(state[0]).split()]) 
        print(state_vector)
        action = self.actor(convertToTensorInput(state_vector, self.state_size)).detach().numpy() 
        # self.actor안에 action_size가 안들어가서 내가 직접 넣었음..!

        noise = self.OU.sample()

        if self.train_mode:
            return action + noise
        else:
            return action


    ##### 메모리에 데이터 추가 함수
    def append_sample(self, state, action, rewards, next_state, done):
        self.memory.append((state, action, rewards, next_state, done))


    ##### 학습 진행 함수
    def train_model(self):
        mini_batch = random.sample(self.memory, batch_size)     # 버퍼에서 batch_size만큼 배치 뽑아 파라미터 업데이트 (학습)

        states      = torch.FloatTensor([sample[0] for sample in mini_batch])
        actions     = torch.FloatTensor([sample[1] for sample in mini_batch])
        rewards     = torch.FloatTensor([sample[2] for sample in mini_batch])
        next_states = torch.FloatTensor([sample[3] for sample in mini_batch])
        dones       = torch.FloatTensor([sample[4] for sample in mini_batch])

        # 타겟을 만들기 위해 action 선택과 평가
        target_actor_actions     = self.target_actor(next_states)   # 각 액션별 확률 (정책함수)
        target_critic_predict_qs = self.target_critic(next_states, target_actor_actions)    # q_val

        target_qs = [reward + discount_factor * (1 - done) * target_critic_predict_q 
                                for reward, target_critic_predict_q, done 
                                in zip(rewards, target_critic_predict_qs, dones)]
        target_qs = torch.FloatTensor([target_qs])

        q_val = self.critic(states, actions)

        critic_loss = torch.mean((q_val - target_qs)**2)
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        actor_loss = -torch.mean(self.critic(states, self.actor(states)))
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()

        self.soft_update_target(self.target_critic, self.critic)
        self.soft_update_target(self.target_actor, self.actor)

        return actor_loss


    ##### soft target 파라미터 업데이트 함수
    def soft_update_target(self, target, orign):
        for target_param, orign_param in zip(target.parameters(), orign.parameters()):
            target_param.data.copy_((1 - tau) * target_param.data + tau * orign_param.data)