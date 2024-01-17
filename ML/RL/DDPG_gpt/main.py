import gym
import torch
from DDPGAgent import DDPGAgent
import numpy as np


# 환경 초기화
env = gym.make('Pendulum-v1')
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
max_action = float(env.action_space.high[0])
# DDPG Agent 초기화
agent = DDPGAgent(state_dim, action_dim, max_action)

# 학습 매개변수 설정
episodes = 100  # 총 에피소드 수
batch_size = 64  # 배치 크기

# 학습 루프
for episode in range(episodes):
    state = env.reset()
    episode_reward = 0

while True:
    # Actor로부터 행동 결정
    # state : (array([ 0.01520265,  0.9998844 , -0.5394536 ], dtype=float32), {})이므로
    # state[0]로 처리
    state  = state[0]
    print(state)
    action = agent.actor(torch.tensor(state).float().unsqueeze(0)).cpu().data.numpy().flatten()
    action = np.clip(action + np.random.normal(0, 0.1, size=action.shape), -max_action, max_action) # 액션에 노이즈 추가
    # 환경에 행동 적용
    print(env.step(action))
    next_state, reward, done, a, b = env.step(action)
    # 경험을 리플레이 버퍼에 저장
    agent.replay_buffer.add((state, action, next_state, reward, done))
    # 상태 업데이트
    state = next_state
    episode_reward += reward

    # 리플레이 버퍼에서 무작위로 배치 샘플링
    if len(agent.replay_buffer.buffer) > batch_size:
        batch = agent.replay_buffer.sample(batch_size)
        batch_states, batch_actions, batch_next_states, batch_rewards, batch_dones = map(np.array, zip(*batch))
        agent.train(batch_states, batch_actions, batch_next_states, batch_rewards, batch_dones)


    if done:
        break

print(f"Episode {episode + 1}: Reward: {episode_reward}")