import torch
from torchvision import datasets, transforms
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# 데이터 전처리
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 데이터셋 로드
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# 특징 벡터와 레이블 추출
X_train = train_dataset.data.view(len(train_dataset), -1).float() / 255.0
y_train = train_dataset.targets

# k-NN 분류기 정의
class KNNClassifier:
    def __init__(self, k):
        self.k = k
        
    def fit(self, X, y):
        self.X = X
        self.y = y
        
    def predict(self, X_test):
        distances = torch.cdist(X_test, self.X)
        _, indices = torch.topk(distances, self.k, dim=1, largest=False)
        k_nearest_labels = self.y[indices]
        predicted_labels, _ = torch.mode(k_nearest_labels, dim=1)
        return predicted_labels
    
# 교차 검증을 위한 k 값 리스트
k_values = [1, 3, 5, 7, 9]

# 정확도를 저장할 리스트
accuracy_list = []

# 각 k 값에 대해 교차 검증 수행
for k in k_values:
    knn = KNNClassifier(k)
    scores = cross_val_score(knn, X_train, y_train, cv=5)
    accuracy = scores.mean()
    accuracy_list.append(accuracy)

# 그래프 그리기
plt.plot(k_values, accuracy_list, marker='o')
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.title('k-NN Cross Validation')
plt.show()