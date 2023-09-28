# Created or modified on May 2022
# Author: 임일
# Factorizagion Machines(FM) 구현

import numpy as np
import pandas as pd
from sklearn.utils import shuffle

# Load the u.data file into a dataframe
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('C:/RecoSys/Data/u.data', sep='\t', names=r_cols, encoding='latin-1') 

# User encoding
user_dict = {}
for i in set(ratings['user_id']):
    user_dict[i] = len(user_dict)
n_user = len(user_dict)
# Item encoding
item_dict = {}
start_point = n_user
for i in set(ratings['movie_id']):
    item_dict[i] = start_point + len(item_dict)
n_item = len(item_dict)
start_point += n_item
num_x = start_point               # Total number of x
ratings = shuffle(ratings, random_state=1)

# Generate X data
data = []
y = []
w0 = np.mean(ratings['rating'])
for i in range(len(ratings)):
    case = ratings.iloc[i]
    x_index = []
    x_value = []
    x_index.append(user_dict[case['user_id']])     # User id encoding
    x_value.append(1)
    x_index.append(item_dict[case['movie_id']])    # Movie id encoding
    x_value.append(1)
    data.append([x_index, x_value])
    y.append(case['rating'] - w0)
    if (i % 10000) == 0:
        print('Encoding ', i, ' cases...')

def RMSE(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true) - np.array(y_pred))**2))

class FM():
    def __init__(self, N, K, data, y, alpha, beta, train_ratio=0.75, iterations=100, tolerance=0.005, l2_reg=True, verbose=True):
        self.K = K          # Number of latent factors
        self.N = N          # Number of x (variables)
        self.n_cases = len(data)            # N of observations
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations
        self.l2_reg = l2_reg
        self.tolerance = tolerance
        self.verbose = verbose
        # w 초기화
        self.w = np.random.normal(scale=1./self.N, size=(self.N))
        # v 초기화
        self.v = np.random.normal(scale=1./self.K, size=(self.N, self.K))
        # Train/Test 분리
        cutoff = int(train_ratio * len(data))
        self.train_x = data[:cutoff]
        self.test_x = data[cutoff:]
        self.train_y = y[:cutoff]
        self.test_y = y[cutoff:]

    def test(self):                                     # Training 하면서 RMSE 계산 
        # SGD를 iterations 숫자만큼 수행
        best_RMSE = 10000
        best_iteration = 0
        training_process = []
        for i in range(self.iterations):
            rmse1 = self.sgd(self.train_x, self.train_y)        # SGD & Train RMSE 계산
            rmse2 = self.test_rmse(self.test_x, self.test_y)    # Test RMSE 계산     
            training_process.append((i, rmse1, rmse2))
            if self.verbose:
                if (i+1) % 10 == 0:
                    print("Iteration: %d ; Train RMSE = %.6f ; Test RMSE = %.6f" % (i+1, rmse1, rmse2))
            if best_RMSE > rmse2:                       # New best record
                best_RMSE = rmse2
                best_iteration = i
            elif (rmse2 - best_RMSE) > self.tolerance:  # RMSE is increasing over tolerance
                break
        print(best_iteration, best_RMSE)
        return training_process
        
    # w, v 업데이트를 위한 Stochastic gradient descent 
    def sgd(self, x_data, y_data):
        y_pred = []
        for data, y in zip(x_data, y_data):
            x_idx = data[0]
            x_0 = np.array(data[1])     # xi axis=0 [1, 2, 3]
            x_1 = x_0.reshape(-1, 1)    # xi axis=1 [[1], [2], [3]]
    
            # biases
            bias_score = np.sum(self.w[x_idx] * x_0)
    
            # score 계산
            vx = self.v[x_idx] * (x_1)          # v matrix * x
            sum_vx = np.sum(vx, axis=0)         # sigma(vx)
            sum_vx_2 = np.sum(vx * vx, axis=0)  # ( v matrix * x )의 제곱
            latent_score = 0.5 * np.sum(np.square(sum_vx) - sum_vx_2)

            # 예측값 계산
            y_hat = bias_score + latent_score
            y_pred.append(y_hat)
            error = y - y_hat
            # w, v 업데이트
            if self.l2_reg:     # regularization이 있는 경우
                self.w[x_idx] += error * self.alpha * (x_0 - self.beta * self.w[x_idx])
                self.v[x_idx] += error * self.alpha * ((x_1) * sum(vx) - (vx * x_1) - self.beta * self.v[x_idx])
            else:               # regularization이 없는 경우
                self.w[x_idx] += error * self.alpha * x_0
                self.v[x_idx] += error * self.alpha * ((x_1) * sum(vx) - (vx * x_1))
        return RMSE(y_data, y_pred)

    def test_rmse(self, x_data, y_data):
        y_pred = []
        for data , y in zip(x_data, y_data):
            y_hat = self.predict(data[0], data[1])
            y_pred.append(y_hat)
        return RMSE(y_data, y_pred)

    def predict(self, idx, x):
        x_0 = np.array(x)
        x_1 = x_0.reshape(-1, 1)

        # biases
        bias_score = np.sum(self.w[idx] * x_0)

        # score 계산
        vx = self.v[idx] * (x_1)
        sum_vx = np.sum(vx, axis=0)
        sum_vx_2 = np.sum(vx * vx, axis=0)
        latent_score = 0.5 * np.sum(np.square(sum_vx) - sum_vx_2)

        # 예측값 계산
        y_hat = bias_score + latent_score
        return y_hat

K = 350
fm1 = FM(num_x, K, data, y, alpha=0.0014, beta=0.075, train_ratio=0.75, iterations=600, tolerance=0.0005, l2_reg=True, verbose=True)
result = fm1.test()

