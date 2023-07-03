# NOTE 1. Plotting
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# 사인과 코사인 곡선의 x,y 좌표를 계산 (0-3파이)
x = np.arange(0, 3 * np.pi, 0.1)

y_sin = np.sin(x)
y_cos = np.cos(x)

# matplotlib를 이용해 점들을 그리기
plt.plot(x, y_sin)
plt.show()  # 그래프를 나타나게 하기 위해선 plt.show()함수를 호출해야만 합니다.

# 여러 개의 그래프와 제목, 범주, 축 이름을 한 번에 쉽게 나타낼 수 있습니다:
# matplotlib를 이용해 점들을 그리기
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])  # 그래프에 범례 추가
plt.show()



# NOTE 2. Subplots
# plt.subplot(num_rows, num_cols, plot_index)
# 좌측 상단 서브플롯의 인덱스는 1, 우측 상단 서브플롯의 인덱스는 2, 좌측 하단 서브플롯의 인덱스는 3, 우측 하단 서브플롯의 인덱스는 4

# 높이가 2이고 너비가 1인 subplot 구획을 설정하고,
# 첫 번째 구획을 활성화.
plt.subplot(2, 1, 1)

# 첫 번째 그리기
plt.plot(x, y_sin)
plt.title('Sine')
plt.show()
# 두 번째 subplot 구획을 활성화 하고 그리기
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# 그림 보이기.
plt.show()



# NOTE 3. 이미지
img = imageio.imread('Python_Numpy_Tutorial/assets/cat.jpg')
img_tinted = img * [1, 0.95, 0.9]

# 원본 이미지 나타내기
plt.subplot(1, 2, 1)
plt.imshow(img)

# 색변화된 이미지 나타내기
plt.subplot(1, 2, 2)

# imshow를 이용하며 주의할 점은 데이터의 자료형이
# uint8이 아니라면 이상한 결과를 보여줄 수도 있다는 것입니다.
# 그러므로 이미지를 나타내기 전에 명시적으로 자료형을 uint8로 형변환 해줍니다.

plt.imshow(np.uint8(img_tinted))
plt.show()