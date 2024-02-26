import gym
from DDPGAgent import DDPGAgent

if __name__ == "__main__":
    env   = gym.make('Pendulum-v1', render_mode="rgb_array")
    agent = DDPGAgent(env)
    agent.run()
    agent.test()