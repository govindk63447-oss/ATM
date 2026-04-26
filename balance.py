import data

def balance_check():
    enter_acc_no=int(input("Enter your account number :"))
    if enter_acc_no==data.account_number[0]:
        enter_pin = int(input("Enter your pin :"))
        if enter_pin == data.pin_data[0]:
            if data.balance==0:
                print("NO balance! jake paisa daal phle gareeb :)")  
            else:
                print(f"your balance is {data.balance}")
    else:
        print("ACCOUNT DOESN'T EXIST, CREATE ONE ")
