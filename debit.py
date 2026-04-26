import data
def debit():
    enter_acc_no=int(input("Enter your account number :"))
    if enter_acc_no==data.account_number[0]:
        enter_pin= int(input("enter your pin :"))
        if enter_pin == data.pin_data[0]:
            debit_amount=float(input("enter amount to debit :"))
            if debit_amount <= data.balance:
                data.balance=data.balance-debit_amount
                print(f"Amount {debit_amount} is debited ")
                data.history.append(f"Rs.{debit_amount} debited. balance = {data.balance}")
                print(f"The remaining balance is Rs.{data.balance}")
            elif data.balance==0:
                print("Zero balance")
            else:
                print(f"NOT ENOUGH MONEY.your balance is {data.balance}")
        else:
            print("chorr ! galat pin hai")
    else:
        print("ACCOUNT DOESN'T EXIST, CREATE ONE ")
 
