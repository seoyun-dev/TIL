import torch.optim as optim
import torch.nn as nn
import torch
import copy
from Actor import Actor
from Critic import Critic
from ReplayBuffer import ReplayBuffer

class DDPGAgent:
    def __init__(self, state_dim, action_dim, max_action):
        self.actor = Actor(state_dim, action_dim, max_action)
        self.actor_target = copy.deepcopy(self.actor)
        self.actor_optimizer = optim.Adam(self.actor.parameters())

        self.critic = Critic(state_dim, action_dim)
        self.critic_target = copy.deepcopy(self.critic)
        self.critic_optimizer = optim.Adam(self.critic.parameters())

        self.replay_buffer = ReplayBuffer()
        self.max_action = max_action

    # 추가적인 메서드는 여기에 정의합니다.
        
    def train(self, batch_states, batch_actions, batch_next_states, batch_rewards, batch_dones, gamma=0.99, tau=0.005):
        states = torch.FloatTensor(batch_states)
        next_states = torch.FloatTensor(batch_next_states)
        actions = torch.FloatTensor(batch_actions)
        rewards = torch.FloatTensor(batch_rewards)
        dones = torch.FloatTensor(batch_dones)

        # Critic 업데이트
        next_actions = self.actor_target(next_states)
        target_Q = self.critic_target(next_states, next_actions)
        target_Q = rewards + (gamma * target_Q * (1 - dones))
        current_Q = self.critic(states, actions)
        critic_loss = nn.MSELoss()(current_Q, target_Q.detach())
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        # Actor 업데이트
        actor_loss = -self.critic(states, self.actor(states)).mean()
        self.actor_optimizer.zero_grad()
        actor_loss.backward()
        self.actor_optimizer.step()

        # 타깃 네트워크 소프트 업데이트
        for param, target_param in zip(self.critic.parameters(), self.critic_target.parameters()):
            target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)

        for param, target_param in zip(self.actor.parameters(), self.actor_target.parameters()):
            target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)