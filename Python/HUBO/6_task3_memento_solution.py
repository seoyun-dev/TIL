from cs1graphics import *
from time import *
import random



# 캔버스 생성
canvas = Canvas(640, 580)
canvas.setTitle("Memento")



# 각 path와 이름을 미리 저장 (path+names를 사용해서 Image를 불러오기 위해서)
path = "./images/"
names = ("pika.PNG", "firi.PNG", "green.PNG",
        "othergreen.PNG", "liza.PNG", "strange.PNG")







# cards 리스트와 num_pads 리스트를 생성, cards 리스트는 그림객체와 (Image 객체) 이름을 Tuple 형태로 저장해놓는 리스트
# num_pads는 0~23까지 숫자가 적힌 카드를 저장해놓는 리스트
# coorect_list는 맞춘 카드를 저장해놓는 리스트 (카드의 순서를 저장)


cards = []  # 이미지
num_pads = []  # 숫자 0~23
correct_list = []  # 맞춘 카드 리스트




# 초기값
tries = 1
time_delay=1




# cards initialization 함수: cards 리스트와 num_pads리스트를 생성
def initialize():
    for i in range(6):
        for k in range(4):
            img = Image(path + names[i])
            temp_tuple = (img, names[i])
            cards.append(temp_tuple)

    for i in range(24):
        card = Layer()
        rect = Rectangle(90, 120, Point(0, 0))
        text = Text(str(i), 18, Point(0, 0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)

    random.shuffle(cards)







# 카드를 보여주는 함수: 맨 처음 canvas 위의 객체들을 다 없애고 (clear),  처음부터 다시 그림
# correct_list에 있는 순서는 cards에서 이미지를 가져오고 아닌 순서는 num_pads에서 가져옴
def print_cards():
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range(len(num_pads)):
        if i in correct_list:
            cards[i][0].moveTo(i_w + w, i_h + h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h + h)
            canvas.add(num_pads[i])

        w += 100
        if w % 600 == 0:
            w = 0
            h += 130







#카드가 유효한지 나타내는 함수
def is_valid(num1, num2):
    return (num1!=num2) and (num1 not in correct_list) and (num2 not in correct_list) and (num1 in range(24)) and (num2 in range(24))   






# 유저가 두개의 순서를 골랐을 때, 두개의 카드가 같은 카드인지 확인하는 함수
# 구체적으로는 correct_list 에 넣어서 print를 함으로써 잠깐 카드를 보여주고 
# 두개의 카드가 다른 카드라면 correct_list 에서 뺀 다음 다시 print를 함
#두개의 카드가 같은 카드인지 안니지를 결과로 냄
def check(num1, num2):
    result=1
    correct_list.append(num1)
    correct_list.append(num2)
    print_cards()
    sleep(time_delay)
    if cards[num1][1]!=cards[num2][1]:
        correct_list.pop()
        correct_list.pop()
        result=0
        print_cards()
    return result































#main
# 맨 처음 모든 이미지를 보여줘야 하므로 아래와 같은 과정을 거침
initialize()
correct_list=range(24)
print_cards()
sleep(5)



#다시 숫자패드를 보여줘야 하므로 아래와 같은 과정을 거침
correct_list = []
print_cards()




print("### Welcome to the Python Memento game!!! ###")




while len(correct_list)!=24:
    print("%d-th try" %tries)
    print("You got %d pairs" %int(len(correct_list)/2))
    input1=int(input("Input the first card number: "))
    input2=int(input("Input the second card number: "))
    if is_valid(input1, input2):
        check_result=check(input1,input2)
        if check_result:
            print("Correct")
        else:
            print("Wrong!")
    tries+=1
