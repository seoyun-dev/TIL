A = int(input("A: "))
N = input("N: ")

B = 0
for i in range(len(N)):
    B += int(N[-i-1]) * A**i

print("B:", B)