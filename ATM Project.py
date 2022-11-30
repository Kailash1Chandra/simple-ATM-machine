a = input("enter your name")
print(a)
print("=======WELCOME TO STATE BANK OF INDIA=======")
import time
print("please insert your card")
time.sleep(5)
Password=12345
pin=int(input("please enter your pin"))
balance=100000
if pin==Password:
    while True:
        print(""" 
                    1 == balance
                    2 == withdrawn_amount
                    3 == deposit balance
                    4 == exit""")
        try:
            option=int(input("please enter your choice"))
        except:
            print("please enter valid option")
            
        if option==1:
            print(f"your updated balance is {balance}")
       
        if option==2:
            withdrawn_amount=int(input("please enter withdraw_amount"))
            balance=balance-withdrawn_amount

            print(f"{withdrawn_amount} is debited from your account")
            print(f"your updated balance is {balance}")

        
        if option==3:
            deposit_amount=int(input("please enter deposit_amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance}")

        if option==4:
            break
else:
    print("please enter the valid pin try again")
