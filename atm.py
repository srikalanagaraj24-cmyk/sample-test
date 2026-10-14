import calc as ca

USER_DATA = {
    "name":"sri",
    "acc no":123456789,
    "pin":1234,
    "total_bal" :10000
}

def user_info():
    if USER_DATA and USER_DATA["username"]:
        return f" hi wlecome user {USER_DATA['username']} your acc.no is {USER_DATA['acc no']}"
    else:
        return False

def withdraw(withdraw_amount):

    if withdraw_amount > USER_DATA["total_bal"]:
        return False
    else:
        amount = ca.withdraw_calc(USER_DATA['total_bal'] , withdraw_amount)
        USER_DATA['total bal'] = amount
        return amount


def deposit(deposit_amount):
        if deposit_amount:
            amount = ca.deposit_calc(USER_DATA["total bal"],deposit_amount)
            USER_DATA["total bal"] = amount
            return amount
        else:
            return False


def check_balance():
    return USER_DATA["total bal"]

def main():
    print("wlecome to ATM")
    print("="*20)

    pin = int(input("enter your pin number:"))

    if pin == USER_DATA["pin"]:
        print(user_info)

while True:
    choice = int(input("1.withdraw\n 2.deposit\n 3.checkbalance\n 4. exit \n enter ur choice"))

    match choice:

        case 1:
            amount = int(input("enter the amount to withdraw:"))
            withdraw_res= withdraw(amount)
            if withdraw_res:
                print("withdraw success , your total balance is:{witthdraw_res}")
            else:
                print("insufficient balance")

        case 2:
            amount = int(input("enter the amount to deposit:"))
            print(f"deposit success , your total bal is:{deposit(amount)}")

        case 3:
            print(f"your total balance is :{check_balance}")   
        case 4:
            print("thanks for using ATM")
            break
        case _:
            print("invalid choice pleacse coose 1 to 4")
            
else:
    print("invalid pin no , please try again")
    return
if __name__ == "__main__":
    main()



