import math

sin = math.sin
pi  = math.pi

def sin_steps(steps):
    # 3개의 값 -> 2 영역 구분, steps+1 개의 값 -> steps개 영역 구분
    for i in range(steps+1):   # i: 0 ~ steps (steps+1 개)
        x = ( float(i) / steps ) * 2 * pi
        print(sin(x))

sin_steps(int(input("number of steps: ")))