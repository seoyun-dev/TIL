a = 17

def test():
    # a가 파라미터로 대입(함수의 지역변수가 됨-원래 a에 영향X)되거나, 
    # global a(전역변수-원래 a에 영향미침)가 아니므로 지역변수
    print (a)   # 할당된 지역변수 없으므로 error
    a = 13
    print (a)

test()  

# global a (at line 5)
