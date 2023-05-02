a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

def is_triange(a, b, c):
    bool_result = False
    if a < b + c and b < a + c and c < a + b:
        bool_result = True
    return bool_result 

if is_triange(a, b, c):
    print("YES")
else:
    print("NO")