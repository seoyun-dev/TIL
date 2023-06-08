class Fourcal:
    def __init__(self, first, second):
        self.first  = first
        self.second = second

    # 위의 생성자없이 아래만 존재할 경우 a=Fourcal()로 argument없이 생성가능
    def setdata(self, first, second):
        self.first  = first
        self.second = second

    def show(self):
        print("난 부모")

    def add(self):
        return self.first + self.second
    
    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second
    
    def div(self):
        return self.first / self.second



# Fourcal 클래스 상속
class MoreFourCal(Fourcal):

    def pow(self):
        super().show()  # 부모클래스의 메소드 쓰기 - super()
        return self.first ** self.second
    
    # 메소드 오버라이딩
    def div(self):
        if self.second == 0:
            return 0
        return self.first / self.second
    


# 부모 클래스 Fourcal
a = Fourcal(4, 1)
print(a.add())
a.setdata(5, 2)
print(a.add())

# 자식 클래스 MoreFourCal
a_child = MoreFourCal(4, 2)
print(a_child.pow())
print(a_child.div())
a_child.setdata(4, 0)
print(a_child.div())