# TODO 파이토치 사용화여, CNN으로 MNIST 학습하는 코드 작성
# [CNN으로 MNIST 분류하기] (https://wikidocs.net/63565)

import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn.init



###################################################### 환경설정

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 랜덤 시드 고정
# 랜덤 시드는 무작위 수열을 생성할 때 사용되는 초기값으로 
# 동일 랜덤시드를 사용하면 항상 같은 순서의 난수들이 생성되어 재현성을 보장
torch.manual_seed(777)

# GPU 사용 가능일 경우 랜덤 시드 고정
if device == 'cuda':
    torch.cuda.manual_seed_all(777)


learning_rate = 0.001
training_epochs = 15
# 히나의 에포크: 전체 학습 데이터셋을 한 번 모델에 대입하고 역전파를 통해 가중치를 조정하는 과정을 의미
batch_size = 100






###################################################### 데이터 전처리

mnist_train = dsets.MNIST(root='MNIST_data/', # 다운로드 경로 지정
                            train=True, # True를 지정하면 훈련 데이터로 다운로드
                            transform=transforms.ToTensor(), # 텐서로 변환
                            download=True)

mnist_test = dsets.MNIST(root='MNIST_data/', # 다운로드 경로 지정
                            train=False, # False를 지정하면 테스트 데이터로 다운로드
                            transform=transforms.ToTensor(), # 텐서로 변환
                            download=True)

# shuffle: 데이터를 미니배치로 나누기 전에 데이터를 섞을지 여부를 결정합. True로 설정하면 매 에포크(epoch)마다 데이터가 랜덤하게 섞임
#drop_last: 데이터를 미니배치로 나눌 때 마지막에 배치 크기보다 작은 크기의 데이터가 남으면 해당 데이터를 버릴지 여부를 결정. True로 설정하면 마지막 배치가 batch_size보다 작을 경우 해당 배치를 버림.
data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
                                            batch_size=batch_size,
                                            shuffle=True,
                                            drop_last=True)





###################################################### CNN 클래스

class CNN(torch.nn.Module):

    def __init__(self):
        super(CNN, self).__init__()
        # 첫번째층
        # 텐서크기 : (배치크기 * 높이 * 너비 * 채널)
        # ImgIn shape=(?, 28, 28, 1)     --- 임의의 텐서 크기
        #    Conv     -> (?, 28, 28, 32) --- 합성곱 층 통과 후 텐서 크기
        #    Pool     -> (?, 14, 14, 32) --- 맥스풀링 통과 후 텐서의 크기
        self.layer1 = torch.nn.Sequential(
            # in_channel=1, out_channel=32 : 1채널을 입력받아 32채널을 뽑아내라. 
            # 3*3 kernel size를 가짐 / stride : 커널을 이동시키는 간격
            torch.nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))    # 풀링: 차원 줄이고 특징 강조(추출)

        # 두번째층
        # ImgIn shape=(?, 14, 14, 32)
        #    Conv      ->(?, 14, 14, 64)
        #    Pool      ->(?, 7, 7, 64)
        self.layer2 = torch.nn.Sequential(
            torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))

        # 전결합층 7x7x64 inputs -> 10 outputs
        self.fc = torch.nn.Linear(7 * 7 * 64, 10, bias=True)

        # 전결합층 한정으로 가중치 초기화
        torch.nn.init.xavier_uniform_(self.fc.weight)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        #전결합층을 위해서 Flatten
        out = out.view(out.size(0), -1)   # 첫 번째 차원인 배치차원 제외하고 나머지 펼치기
        out = self.fc(out)
        return out





###################################################### 분류기, 손실함수, 최적화 환경 설정

# 분류기
# CNN 모델 정의
# .to() :  모델과 입력 데이터를 지정하 곳으로 옮겨 더 빠르게 학습 가능
model = CNN().to(device)

# 손실함수
criterion = torch.nn.CrossEntropyLoss().to(device)  # 비용 함수에 소프트맥스 함수 포함되어져 있음.
# 최적화 - Adam : SGD의 한 종류 / parameters(): 최적화할 모델의 매개변수들
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

total_batch = len(data_loader)
print('총 배치의 수 : {}'.format(total_batch))





##################################### CNN(score)->Softmax(loss)->Adam(SGD,최적화)->parameter update

# for epoch하나 in 전체 에포크:
for epoch in range(training_epochs):
    avg_cost = 0

    # for 배치하나 안의 데이터 in 하나의 배치:
    for X, Y in data_loader: # 미니 배치 단위로 꺼내온다. X는 미니 배치, Y는 레이블.
        # image is already size of (28x28), no reshape
        # label is not one-hot encoded
        X = X.to(device)
        Y = Y.to(device)

        optimizer.zero_grad()   # 매 학습마다 계산 전에 기울기 0으로 초기화
        # forward pass
        hypothesis = model(X)           # CNN으로 score(예측값) 구하기
        cost = criterion(hypothesis, Y) # 예측값과 실제 정답(Y) 사이의 손실(by Softmax(criterion))
        # Backpropagation
        cost.backward()                 # 손실에 대한 Backpropagation 수행
        # Parameter update
        optimizer.step()                # 최적화 알고리즘(Adam)을 사용하여 모델의 매개변수를 업데이트

        avg_cost += cost / total_batch

    print('[Epoch: {:>4}] cost = {:>.9}'.format(epoch + 1, avg_cost)) #






###################################################### CNN 이용하여 실제 분류

# 학습을 진행하지 않을 것이므로 torch.no_grad()
with torch.no_grad():       # 컨택스트 매니저, 평가 단계에서 그라디언트 계산을 비활성화 for 속도, 메모리
    # mnist_test에서 이미지를 가져와 4차원 텐서로 변환 -> 텐서 지정한 장치로 이동
    X_test = mnist_test.test_data.view(len(mnist_test), 1, 28, 28).float().to(device)
    Y_test = mnist_test.test_labels.to(device)

    prediction = model(X_test)                    # prediction : 각 샘플에 대해 클래스별 확률 값
    correct_prediction = torch.argmax(prediction, 1) == Y_test
    # argmax() :  1차원 텐서에서 특정 차원에 대해 최댓값을 갖는 인덱스를 반환
    # 1 : 각 샘플(배치)의 클래스방향에 대해 최댓값을 구함
    accuracy = correct_prediction.float().mean()  # Boolean tensor to float(1.0/0.0)비율 tensor
    print('Accuracy:', accuracy.item())           # .item(): 텐서에서 하나의 스칼라 값을 얻어냄