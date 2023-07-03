N = int(input("N: "))


for i in range(1, N+1):
    print(" "*(N-i) + "*" *(2*i-1) + " "*(N-i))

for i in range(N-1, 0, -1):
    print(" "*(N-i) + "*" *(2*i-1) + " "*(N-i))