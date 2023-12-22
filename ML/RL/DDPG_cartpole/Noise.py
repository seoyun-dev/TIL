import numpy as np
import numpy.random as nr

mu    = 0
theta = 0.15
sigma = 0.3


# 일반적을 이산적인 action space에서는 Epsilon-greedy 기법으로 랜덤한 action이 가능하다. 
# 그러나 continuous 한 action space에서는 랜덤하게 actions을 취하는거이 무척 어렵다.
# 그러므로 action에 Noise를 첨가하여 효과적인 학습이 가능하게 한다.
class OU_noise:
    def __init__(self, action_size):
        self.action_dimension = action_size
        self.mu               = mu
        self.theta            = theta
        self.sigma            = sigma
        self.state            = np.ones(self.action_dimension) * self.mu
        self.reset()

    def reset(self):
        self.state = np.ones(self.action_dimension) * self.mu

    def sample(self):
        x          = self.state
        dx         = self.theta * (self.mu - x) + self.sigma * nr.randn(len(x))
        self.state = x + dx
        return self.state