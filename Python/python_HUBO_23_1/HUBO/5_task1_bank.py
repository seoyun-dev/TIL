# def deposit(money):
#     global balance
#     balance += money
#     return balance

# def withdrawal(money):
#     global balance
#     balance -= money
#     return balance

# def balance_check():
#     global balance
#     return balance

# def bank():
#     global balance
#     answer = input("Deposit(d) or withdrawal(w) or balance check(c)?? ")
#     if answer == "":
#         return answer
#     elif answer == "d":
#         money = int(input("How much do you want to deposit? "))
#         deposit(money)
#         print("You deposited", money, "won")
#     elif answer == "w":
#         money = int(input("How much do you want to withdraw? "))
#         if balance >= money:
#             withdrawal(money)
#             print("You've withdrawn", money, "won")
#         else:
#             print("You've withdrawn", money, "won")
#             print("But you only have", balance, "won")
#     elif answer == "c":
#         print("Your current balance is", balance_check(), "won")
#     else:
#         print("Please, press d or w or return")

# balance = 0

# answer = 'empty'
# while answer != "":
#     answer = bank()


balance = 0

def deposit(money):
    global balance
    balance += money
    print("입금 금액 {}".format(money))
    
def withdrawal(money):
    global balance
    if balance >= money:
        balance -= money
        print("출금금액 {}".format)
    else:
        print("너는 {}을 인출하려고 했음".format(money))
        print("하지만 너의 잔액은 {}야. 욕심 ㄴㄴ".format(balance))
    

def bank():
    global balance
    while True:
        answer = input("d or w or c ?")
        if answer == '':
            return
        elif answer == 'w':
            withdrawal(int(input("얼마?")))
        elif answer == 'd':
            deposit(int(input("얼마?")))
        elif answer == 'c':
            print("현재 잔액은 {}임".format(balance))
        else:
            print("d w c 중에 입력하거나 공백 입력해서 끝내")

bank()







