from cs1graphics import *
from time import *
import random

### Canvas 생성 
canvas = Canvas(640, 580)
canvas.setTitle("Memento")


# 메멘토게임을 위한 6가지 이미지 호출을 위한, 이름과 경로정의 (가로 90pixel, 세로 120pixel이어야 함)
path  = "./실습자료_6_그림/"
names = ("pika.PNG", "firi.PNG", "green.PNG", "othergreen.PNG", "liza.PNG", "strange.PNG")


# 그림카드/숫자카드 리스트 생성 (cards, num_pads)
cards        = []  # 그림카드: 이미지
num_pads     = []  # 숫자카드: 0~23
correct_list = []  # 맞춘 카드 리스트


# 카드 초기화
def initialize():
    for i in range(6):
        for k in range(4):
            img        = Image(path + names[i])
            temp_tuple = (img, names[i])
            cards.append(temp_tuple)

    for i in range(24):
        card = Layer()
        rect = Rectangle(90, 120, Point(0, 0))
        text = Text(str(i), 18, Point(0, 0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)

    # 그림 카드 순서 섞기
    random.shuffle(cards)


# correct_list에 있는 카드들은 cards 리스트에 있는 이미지를 프린트하고 아닌 카드들은 num_pads에 있는 숫자카드를 프린트
def print_cards():
    canvas.clear()
    w   = 0
    h   = 0
    i_w = 70
    i_h = 90
    for i in range(len(num_pads)):
        if i in correct_list:
            cards[i][0].moveTo(i_w + w, i_h + h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h + h)
            canvas.add(num_pads[i])

        # 한 줄 넘치면 다음 줄로 이동
        w += 100
        if w % 600 == 0:
            w = 0
            h += 130


#확인하는 두 개의 수가 valid (유효한) 한 수인지 확인하는 함수
############### TASK-1) num1과 num2가 1) range(24)의 범위안에 있는 수인지, 2) 두 수가 다른지, 3) 두 수 중 어느 하나라도 coorect list 에 있는지 확인해서 1)-3) 모두 T인 경우에 T 아닐 떄 F를 반환하시오
def is_valid(num1, num2):
    return (num1 in range(24)) and (num2 in range(24)) and (num1 != num2) and (num1 not in correct_list) and (num2 not in correct_list)




#두 개의 수를 확인하는 함수 
############# TASK-2) 아래에 해당하는 코드를 작성하시오
############# 1) num1과 num2에 해당하는 카드는 그림을 보여주면서 screen을 보여라 
############# 2) 두 개의 카드가 같은 카드라면, 두 카드를 correct list에 넣으시오
############# 3) 그렇지 않다면 원래 screen을 보여라
############# 4) 맞췄다면 T, 아니라면 F를 그 결과로 반환하라
def check(num1, num2):
    correct_list.append(num1)
    correct_list.append(num2)
    print_cards()
    sleep(5)
    if cards[num1][1] != cards[num2][1]:
        correct_list.pop()
        correct_list.pop()
        print_cards()
        return 0
    return 1





#초기화 하는 코드, 맨 처음 initialize()를 통하여 카드 생성
initialize()
############# TASK-3) 24개의 모든 그림을 보여주고 10초간 정지 
correct_list = [i for i in range(24)]
print_cards()
sleep(3)
# 이제 게임을 시작해야 하므로 correct_list 를 모두 비우고, 숫자카드들로만 이루어진 screen을 보여준다.
correct_list = []
print_cards()




# main 실행문
print("### Welcome to the Python Memento game!!! ###")
tries = 1
############ Task-4) while 문을 사용하여 모든 카드를 맞출 때까지 게임을 계속한다.
############ 이곳에 작성될 코드는 실습자료를 참고하여 작성하시오 (hint: 위에서 정의된 함수 (is_valid와 check)를  잘 사용하시오!)
############ 한번 시도할 때 마다 tries 를 높인다.
while (len(correct_list) != 24):
    num1 = int(input("Input the first card number: "))
    num2 = int(input("Input the second card number: "))
    if is_valid(num1, num2):
        result = check(num1, num2)
        if result:
            print("Correct!")
        else:
            print("Wrong.....")
    print('%dst try. You got %d pairs.' % (tries, len(correct_list)/2))
    tries += 1