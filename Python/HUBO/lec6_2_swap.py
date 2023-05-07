def swap(a, b):
    # 지역변수 a, b -> 전역변수 x, y에 영향X
    a, b = b, a
    print (a, b)
    
x, y = 123, 456
swap(x, y)      # 456 123
print (x, y)    # 123 456



# return a, b (at line 4)
# x, y = swap(x, y) (replace line 6)