import torch
import torch.nn as nn


# Critic 신경망 정의
class Critic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(Critic, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(state_dim, 128),
                                    nn.ReLU())
        self.layer2 = nn.Sequential(nn.Linear(129, 128),
                                    nn.ReLU())
        self.layer3 = nn.Sequential(nn.Linear(128, 128),
                                    nn.ReLU())
        self.layer4 = nn.Sequential(nn.Linear(128, 1))
        # self.fc1 = nn.Linear(state_dim + action_dim, 64)
        # self.fc2 = nn.Linear(64, 32)
        # self.fc3 = nn.Linear(32, 1)

    def forward(self, state, action):
        x = self.layer1(state)

        is_nested = any(isinstance(a_action, list) for a_action in action)

        if not is_nested:
            # 단일 요소 리스트로 변환
            modified_list = [[a_action] for a_action in action]
            action_final_list = torch.cat([torch.tensor(a) for a in modified_list]).squeeze().unsqueeze(1)
        
        x = torch.cat([x, action_final_list], dim=-1)

        x = self.layer2(x)
        x = self.layer3(x)
        q_val = self.layer4(x)
        # x = self.layer1(state)
        # x = torch.cat([state, action], 1)
        # x = torch.relu(self.fc1(x))
        # x = torch.relu(self.fc2(x))
        # x = self.fc3(x)
        return q_val