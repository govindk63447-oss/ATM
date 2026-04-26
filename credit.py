import data

def credit():
    enter_acc_no=int(input("Enter your account number :"))
    if enter_acc_no==data.account_number[0]:
        enter_pin=int(input("Enter your pin :"))
        if enter_pin==data.pin_data[0]:
            credit_amount=float(input("enter amount to credit :"))
            data.balance=data.balance+credit_amount
            data.history.append(f"Rs.{credit_amount} credited. balance = {data.balance}")
            print(f"the amount of {credit_amount} is credited.your total balance is {data.balance}")
        else:
            print("you have entered the wrong pin!")
    else:
        print("ACCOUNT DOESN'T EXIST, CREATE ONE ")
