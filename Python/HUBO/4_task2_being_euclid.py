def is_triange(a, b, c):
    bool_result = False
    if a < b + c:
        if b < a + c:
            if c < a + b:
                bool_result = True
    return bool_result 

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

if is_triange(a, b, c):
    print("YES")
else:
    print("NO")