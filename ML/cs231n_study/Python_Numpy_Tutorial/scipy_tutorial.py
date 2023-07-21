#numpy를 바탕으로 만들어진 SciPy는, numpy 배열을 다루는 많은 함수를 제공하며 다양한 과학, 공학분야에서 유용하게 사용됩니다.
#SciPy에 익숙해지는 최고의 방법은 SciPy 공식 문서를 보는 것입니다. 이 문서에서는 scipy중 cs231n 수업에서 유용하게 쓰일 일부분만을 소개할것입니다.

# NOTE 1. 이미지 작업
# SciPy는 이미지를 다룰 기본적인 함수들을 제공합니다. 예를들자면, 디스크에 저장된 이미지를 numpy 배열로 읽어 들이는 함수가 있으며, numpy 배열을 디스크에 이미지로 저장하는 함수도 있고, 이미지의 크기를 바꾸는 함수도 있습니다. 이 함수들의 간단한 사용 예시입니다:

# scipy 1.2.0 version이후 부터 imread, imsave, imresize 지원x
from imageio import imread, imsave
# imresize 대체 - PIL.Image.resize()
from PIL import Image
import numpy as np

# JPEG 이미지를 numpy 배열로 읽어들이기
img = imread('Python_Numpy_Tutorial/assets/cat.jpg')
print (img.dtype, img.shape)  # 출력 "uint8 (400, 248, 3)"

# 각각의 색깔 채널을 다른 상수값으로 스칼라배함으로써
# 이미지의 색을 변화시킬 수 있습니다.
# 이미지의 shape는 (400, 248, 3)입니다;
# 여기에 shape가 (3,)인 배열 [1, 0.95, 0.9]를 곱합니다;
# numpy 브로드캐스팅에 의해 이 배열이 곱해지며 붉은색 채널은 변하지 않으며,
# 초록색, 파란색 채널에는 각각 0.95, 0.9가 곱해집니다
img_tinted_arr = img * [1, 0.95, 0.9]

# 데이터 타입을 uint8로 변환(fromarray가 uint8 배열 처리(이전엔 float64)) -> 배열을 이미지로 변환
img_tinted = Image.fromarray(np.uint8(img_tinted_arr))
# 색변경 이미지를 300x300픽셀로 크기 조절
# image.resize((new_width, new_height), resample=Image.BILINEAR)
img_tinted = img_tinted.resize((300,300))


# 색변경 이미지를 디스크에 기록하기
imsave('Python_Numpy_Tutorial/assets/cat_tinted.jpg', img_tinted)



# NOTE 2. MATLAB 파일
# scipy.spatial.distance.pdist함수는 주어진 점들 사이의 모든 거리를 계산
from scipy.spatial.distance import pdist, squareform

# 각 행이 2차원 공간에서의 한 점을 의미하는 행렬을 생성:
# [[0 1]
#  [1 0]
#  [2 0]]
x = np.array([[0, 1], [1, 0], [2, 0]])
print (x)

# x가 나타내는 모든 점 사이의 유클리디안 거리를 계산.
# d[i, j]는 x[i, :]와 x[j, :]사이의 유클리디안 거리를 의미하며,   
# d는 아래의 행렬입니다:
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]
# pdist() 함수는 계산된 거리를 직접 반환하는 것이 아니라, 계산 효율성을 위해 압축된 형식인 condensed distance matrix를 반환합니다. 이후에 계산된 거리를 사용할 때는 squareform() 함수를 사용하여 다시 확장해야 합니다.
d = squareform(pdist(x, 'euclidean'))
print (d)