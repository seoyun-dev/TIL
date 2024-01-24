import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

from Actor import Actor
from Critic import Critic
from Noise import OU_noise


####### DDPG Agent 클래스

class DDPGAgent:
    def __init__(self, env):
        self.env              = env
        self.state_dim        = env.observation_space.shape[0]  # 3
        self.action_dim       = env.action_space.shape[0]       # 1
        self.action_bound     = env.action_space.high[0]        # 2.0 / -1~1 -> -2~2로 액션범위 변화 위해
        
        self.OU            = OU_noise(self.action_dim)
        self.actor         = Actor(self.state_dim, self.action_dim, self.action_bound)
        self.actor_target  = Actor(self.state_dim, self.action_dim, self.action_bound)
        self.critic        = Critic(self.state_dim, self.action_dim)
        self.critic_target = Critic(self.state_dim, self.action_dim)
        
        self.actor_optimizer  = optim.Adam(self.actor.parameters(), lr=1e-4)
        self.critic_optimizer = optim.Adam(self.critic.parameters(), lr=5e-4)
        
        self.memory           = []          # 리플레이 버퍼
        self.batch_size       = 64          # 배치 사이즈  
        self.gamma            = 0.99        # 감쇠인자    
        self.tau              = 0.00001       # soft target network update 파라미터

        self.update_target_models(tau=1)    # 타겟 파라미터들 초기화 (actor, critic과 같도록)


    ##### soft target 파라미터 업데이트 함수
    def update_target_models(self, tau=None):
        if tau is None:
            tau = self.tau
        # 타겟 파라미터 업데이트
        for target_param, param in zip(self.actor_target.parameters(), self.actor.parameters()):
            target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)
        for target_param, param in zip(self.critic_target.parameters(), self.critic.parameters()):
            target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)


    ##### 리플레이 버퍼에 데이터 추가하는 함수 
    def remember(self, state, action, reward, new_state, done):
        self.memory.append([state, action, reward, new_state, done])


    ##### 학습(업데이트) 진행 함수 
    def train(self):
        if len(self.memory) < self.batch_size:
            return

        samples         = random.sample(self.memory, self.batch_size)    # 리플레이버퍼에서 무작위 샘플 추출
        states_list     = []
        actions_list    = []
        rewards_list    = []
        new_states_list = []
        dones_list      = []

        for sample in samples:
            state     = sample[0]
            action    = sample[1][0]
            reward    = sample[2]
            new_state = sample[3]
            done      = sample[4]

            states_list.append(state)
            actions_list.append(action)
            rewards_list.append(reward)
            new_states_list.append(new_state)
            dones_list.append(done)

        
        # 각 리스트를 NumPy 배열로 변환
        states     = torch.tensor(np.vstack(states_list), dtype=torch.float32)
        actions    = torch.tensor(actions_list, dtype=torch.float32)
        rewards    = torch.tensor(rewards_list, dtype=torch.float32)
        new_states = torch.tensor(np.vstack(new_states_list), dtype=torch.float32)
        dones      = torch.tensor(dones_list, dtype=torch.float32)

        # 원 코드
        # batch      = np.array(samples)
        # states     = torch.tensor(np.vstack(batch[:, 0]), dtype=torch.float32)
        # actions    = torch.tensor(list(batch[:, 1]), dtype=torch.float32)
        # rewards    = torch.tensor(list(batch[:, 2]), dtype=torch.float32)
        # new_states = torch.tensor(np.vstack(batch[:, 3]), dtype=torch.float32)
        # dones      = torch.tensor(list(batch[:, 4]), dtype=torch.float32)

        # 타겟 액션, 타겟 Q값 구하기
        target_actions  = self.actor_target(new_states) # 액터(정책함수)-예측된 액션 값
        future_q_values = self.critic_target(new_states, target_actions)    # 크리틱(액션가치함수)
        target_q_values = rewards + (1 - dones) * self.gamma * future_q_values.detach()     # 타겟 Q값 계산

        # actor, critic 파라미터 손실 계산 및 역전파
        # print((self.critic(states,actions)).shape, target_q_values.shape)
        critic_loss = torch.mean((target_q_values-self.critic(states, actions))**2)
        # critic_loss = nn.MSELoss()(self.critic(states, actions), target_q_values.unsqueeze(1))
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()
        
        actor_loss = -self.critic(states, self.actor(states)).mean() # 정책의 목적함수는 정책함수의 가치 > maximize해야 > - 붙임
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()

        # actor, critic 파라미터 업데이트
        self.update_target_models()


    ##### 학습을 실행하는 메인 루프 함수
    def run(self, max_episodes=1000):
        for ep in range(max_episodes):
            state          = self.env.reset()
            episode_reward = 0
            done           = False
            s = 0
            # TODO 왜지.. done이 True가 나오지 않으므로 안끝남; 
            # while not done:
            for trans in range(200):
                self.env.render()

                # state 전처리
                if type(state) == tuple:
                    # state를 튜플 내의 배열로부터 가져옴
                    state_array = state[0]
                    # 배열 내의 요소들을 가져와서 처리
                    value_1 = state_array[0]    # state
                    value_2 = state_array[1]    # action    
                    value_3 = state_array[2]    # reward
                    # 가져온 값들을 원하는 형태로 처리 (예: numpy 배열로 변환)
                    state   = np.array([value_1, value_2, value_3], dtype=np.float32)
                
                state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)

                # action 선택 (by actor, noise)
                action = self.actor(state_tensor).squeeze(0).detach().numpy()
                action = action + self.OU.sample()
                # action = np.clip(action + np.random.normal(0, 0.1, size=action.shape), -self.action_bound, self.action_bound)
                new_state, reward,done, a, b = self.env.step(action)

                # 한 transition 데이터 저장
                self.remember(state, action, reward, new_state, done)
                episode_reward += reward
                state           = new_state

                if len(self.memory) > self.batch_size:
                    self.train()

                if done:
                    break

            # 1000 trans마다 출력
            print(f"200 trans: {ep + 1}, Reward: {episode_reward}")

            if episode_reward > -300:  # Pendulum-v1의 평가 기준
                print(f"Solved at episode {ep + 1}!")
                break

        self.env.close()


    
    def test(self, test_episodes=100):
        for episode in range(test_episodes):
            state = self.env.reset()
            episode_reward = 0
            for t in range(10):
                action = self.actor(state)
                state, reward, done, _ = self.env.step(action)
                episode_reward += reward
                if done:
                    break
            print(f"Episode: {episode + 1}, Reward: {episode_reward}")