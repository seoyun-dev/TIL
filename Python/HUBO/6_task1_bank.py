def deposit(money):
    global balance
    balance += money
    return balance

def withdrawal(money):
    global balance
    balance -= money
    return balance

def balance_check():
    global balance
    return balance

def bank():
    global balance
    answer = input("Deposit(d) or withdrawal(w) or balance check(c)?? ")
    if answer == "":
        return 
    elif answer == "d":
        money = int(input("How much do you want to deposit? "))
        deposit(money)
        print("You deposited", money, "won")
    elif answer == "w":
        money = int(input("How much do you want to withdraw? "))
        if balance >= money:
            withdrawal(money)
            print("You've withdrawn", money, "won")
        else:
            print("You've withdrawn", money, "won")
            print("But you only have", balance, "won")
    elif answer == "c":
        print("Your current balance is", balance_check(), "won")
    else:
        print("Please, press d or w or return")

balance = 0

answer = 'empty'
while answer != "":
    answer = bank()