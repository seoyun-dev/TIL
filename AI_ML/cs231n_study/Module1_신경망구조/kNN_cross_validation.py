import torch
import numpy as np
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# KNN 분류기 정의
class KNNClassifier:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X = X      # 훈련 데이터
        self.y = y      # 라벨

    def predict(self, X_test):
        # 두 텐서간의 거리
        distances = torch.cdist(X_test, self.X)   
        # 가장 distances가 가까운(작은) k개의 값과 해당 인덱스 반환 (dim=1: 행 기준)                      
        _, indices = torch.topk(distances, self.k, dim=1, largest=False) 
        # k_nearest_labels = 장 가까운 k개 이웃의 레이블 
        k_nearest_labels = self.y[indices]
        # torch.mode: 예측된 레이블의 최빈값 반환
        predicted_labels, _ = torch.mode(k_nearest_labels, dim=1)
        return predicted_labels




# MNIST 데이터셋 전처리 파이프라인 (주로, 이미지 데이터)
transform = transforms.Compose([
    transforms.ToTensor(),                  # 입력 데이터를 tensor로 변환
    transforms.Normalize((0.5,), (0.5,))    # 정규화 for 모델 학습, 성능 향상
])


# MNIST 데이터셋 로드
# download: 데이터셋을 인터넷에서 다운로드할지 여부를 결정
# transform: 데이터셋에 적용할 변환(transform) 함수
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)


# 데이터 로더 생성: 데이터 로더는 데이터셋을 미니배치로 나누고, 데이터를 병렬적으로 로드하여 모델 학습 또는 테스트에 활용할 수 있도록 도와줌
# batch_size: 한 번에 처리할 샘플의 양
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)


# 훈련 데이터 준비
# X_train = shape(데이터 개수, 이미지 크기)인 2차원 텐서. 각 행은 하나의 이미지를 나타내며, 각 열은 해당 이미지의 픽셀 값을 나타냄
# train_dataset.data는 MNIST 데이터셋의 이미지 데이터를 나타내는 텐서
# view(len(train_dataset), -1): 텐서의 모양을 (len(train_dataset), -1)로 변환하는 연산. -1은 해당 차원의 크기를 자동으로 계산하도록 하는 특수한 값. 
# 따라서 view(len(train_dataset), -1)는 원래 이미지 데이터의 크기를 유지하면서 첫 번째 차원을 len(train_dataset)로 설정하고, 두 번째 차원은 자동으로 계산하여 설정
# view(): 텐서의 형태 변경하는 메서드 (이미지는 3차원 텐서 형태)
# /255.0: 픽셀 값 정규화 작업 0~255 -> 0~1
X_train = train_dataset.data.view(len(train_dataset), -1).float() / 255.0
y_train = train_dataset.targets


# 테스트 데이터 준비
X_test = test_dataset.data.view(len(test_dataset), -1).float() / 255.0
y_test = test_dataset.targets


k_values = [1, 3, 5, 7, 9]  # k 값들
n_splits = 5                # 교차 검증 폴드 수


# 교차 검증 및 정확도 기록
accuracies = []
std_deviations = []
for k in k_values:
    fold_accuracies = []
    fold_size = len(X_train) // n_splits
    for i in range(n_splits):
        # 검증 데이터와 학습 데이터 분할
        val_start = i * fold_size
        val_end = (i + 1) * fold_size
        X_val = X_train[val_start:val_end]
        y_val = y_train[val_start:val_end]
        # 학습을 위해 검증셋 제외한 훈련데이터 준비
        X_train_cat = torch.cat([X_train[:val_start], X_train[val_end:]])
        y_train_cat = torch.cat([y_train[:val_start], y_train[val_end:]])
        
        # k-NN 모델 학습
        knn = KNNClassifier(k)
        knn.fit(X_train_cat, y_train_cat)
        
        # 검증 데이터셋 정확도 기록
        predictions = knn.predict(X_val)
        accuracy = torch.sum(predictions == y_val).item() / len(y_val) * 100
        fold_accuracies.append(accuracy)
    
    # 특정 k에 대한 검증 셋의 정확도 점 그리기
    for accuracy in fold_accuracies:
        plt.scatter(k, accuracy, c='r')

    # 폴드별 정확도 평균 및 표준편차 계산
    mean_accuracy = np.mean(fold_accuracies)
    std_deviation = np.std(fold_accuracies)
    accuracies.append(mean_accuracy)
    std_deviations.append(std_deviation)
    # NOTE 표준오차 -std_errors.append(std_deviation / np.sqrt(n_splits))
    # n_splits가 많아질수록 표준편차는 당연히 줄어든다. 그렇게 되면 n마다 객관적인 표준편차를 구하기 힘들어지므로 np.sqrt(n_splits)로 나눠주게 된다.
    # 고로 표준오차를 쓰는 것이 더 좋다.


# 그래프 그리기
plt.errorbar(k_values, accuracies, yerr=std_deviations, fmt='o-', color='b', ecolor='g')

plt.xlabel('k')
plt.ylabel('Accuracy')
plt.title('Cross-Validation Accuracy of k-NN')
plt.xticks(k_values)

plt.show()