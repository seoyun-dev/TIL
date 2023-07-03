import math

sin = math.sin
pi  = math.pi

def sin_steps(steps):
    for i in range(steps+1):
        x = (float(i) / steps) * 2 * pi
        # steps=80일 때
        # sin(x)=-1 -> sharp_len=0, sin(x)=0 -> sharp_len=40, sin(x)=1 -> sharp_len=80
        sharp_len = int((sin(x) + 1) * steps)
        print ("#" * sharp_len)

sin_steps(int(input("number of steps: ")))