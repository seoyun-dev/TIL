class Cal:
    def __init__(self, first, second):
        self.first  = first
        self.second = second

    def add(self):
        return self.first + self.second
    
    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second
    
    def div(self):
        return self.first / self.second


# Cal 클래스 상속
class Cal2(Cal):
    # 메소드 오버라이딩
    def div(self):
        if self.second == 0:
            return 0
        return super().div()
    

son = Cal2(2, 0)
print(son.div())