import create
import credit
import debit
import balance
import transaction

def boj():
    while True:
        print("1.CREATE ACCOUNT :")
        print("2.BALANCE ENQUIRY :")
        print("3.DEBIT MONEY :")
        print("4.CREDIT MONEY :")
        # print("5.CALCULATE INTEREST :")
        print("5.TRANSACTION HISTORY :")
        print("6.EXIT :")
        # print("8. :")
        
        choice=int(input("ENTER YOUR CHOICE :"))

        if choice==1:
            create.create()
        elif choice==2:
            balance.balance_check()
        elif choice==3:
            debit.debit()
        elif choice==4:
            credit.credit()
        elif choice==5:
            transaction.tran_his()
        elif choice==6:
            print("thanks for visiting !!")
            break
        else:
            print("invalid choice")
            
boj()
