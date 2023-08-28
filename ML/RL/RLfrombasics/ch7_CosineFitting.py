import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # 인풋(앞 레이어의 노드)=1개, 아웃풋(뒤 레이어의 노드)=128개 -> 128*1 w 필요
        self.fc1 = nn.Linear(1, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 128)
        self.fc4 = nn.Linear(128, 1, bias=False)

    def forward(self, x):
        # 실제로 연산될 때 호출되는 함수
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

def true_fun(X):
    # 데이터 생성 함수. 실제로 학습시키는 우리는 알 수 없지만 데이터 생성을 위해 함수로 표현
    noise = np.random.rand(X.shape[0]) * 0.4 - 0.2
    return np.cos(1.5 * np.pi * X) + X + noise

def plot_results(model):
    # 실제데이터와 학습시킨 모델의 예측치를 그래프로 그리는 코드
    x = np.linspace(0, 5, 100)  # 0~5 사이 숫자를 100개의 등간격으로 뽑안 인풋
    input_x = torch.from_numpy(x).float().unsqueeze(1)
    plt.plot(x, true_fun(x), label="Truth")
    plt.plot(x, model(input_x).detach().numpy(), label="Prediction")
    plt.legend(loc='lower right',fontsize=15)
    plt.xlim((0, 5))
    plt.ylim((-1, 5))
    plt.grid()
    plt.show()

def main():
    data_x = np.random.rand(10000) * 5 # 0~5 사이 숫자 1만개를 샘플링하여 인풋으로 사용 
    model = Model()                    # 뉴럴넷
    optimizer = optim.Adam(model.parameters(), lr=0.001)   # 손실함수
    
    plot_results(model)        # 피팅 되기 전 함수

    for step in range(10000):
        # 뉴럴넷 학습은 미니배치 단위로 이루어짐!
        batch_x = np.random.choice(data_x, 32) # 랜덤하게 뽑힌 32개의 데이터로 mini-batch를 구성
        # x to Tensor + 실수형 + 1차원(batch_size*1)
        batch_x_tensor = torch.from_numpy(batch_x).float().unsqueeze(1) 
        pred = model(batch_x_tensor)    # 데이터 32개의 예측값

        batch_y = true_fun(batch_x)     # 데이터 32개의 실제값
        truth = torch.from_numpy(batch_y).float().unsqueeze(1)
        loss = F.mse_loss(pred, truth) # 데이터마다 MSE 계산 (32개의 값)
        
        optimizer.zero_grad() 
        loss.mean().backward() # 역전파로 그라디언트 계산 (손실 32개의 평균값을 편미분)
        optimizer.step()       # 파라미터 업데이트

    plot_results(model)         # 피팅 된 함수

if __name__ == '__main__':
    main()