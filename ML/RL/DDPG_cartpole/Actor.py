import torch.nn as nn

# 액터 - 정책 네트워크
class Actor(nn.Module):
    def __init__(self, state_size, action_size):
        super(Actor, self).__init__()

        self.layer1 = nn.Sequential(nn.Linear(state_size, 128),
                                    nn.ReLU())
        self.layer2 = nn.Sequential(nn.Linear(128, 128),
                                    nn.ReLU())
        self.layer3 = nn.Sequential(nn.Linear(128, action_size),
                                    nn.Tanh()) 
        # TODO 왜 tanh지? 정책네트워크면 확률이라 -1~1인 tanh가 아니라 softmax여야 하는거 아닌가?

    def forward(self, state):
        x = self.layer1(state)
        x = self.layer2(x)
        action = self.layer3(x)     # 각 액션의 확률 (정책함수)

        return action