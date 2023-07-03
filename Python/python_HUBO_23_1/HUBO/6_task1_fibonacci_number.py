fibonacci = [0, 1]

while fibonacci[-1] < 1000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

fibonacci.pop()
print(fibonacci)