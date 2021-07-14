from typing import OrderedDict


print("welcome to this ATM")
print("please Insert your card")
user_password=1542
user_balance = int(1000)
print("please provide your pin")
password_try = 3
while password_try > 0: 
    password=int(input("please enter your pin:"))
    if password == user_password:
        user_input=input("Enter:\n w for Withdrawl\n d for deposit\n b for balance Enquiry\n q for cancel\n:")
        if user_input == "w":
            withdrawl_amount =int(input("write the amount in multiples of 10: "))
            if withdrawl_amount%10 == 0:
                print(f"please collect your cash\n your available balance is :${user_balance-withdrawl_amount}\nThank you for using this ATM\n")
                break
            else:
                print("give amount in multiples of 10 only")
                break             
        if user_input == "d":
            deposit_amount =int(input("write the amount in multiples of 10: "))
            if deposit_amount%10 ==0:
                print(f"yur balance is $ {deposit_amount+user_balance}\nplese coolect your card")
                break
            else:
                print("give amount in multiples of 10 only")
                break
        if user_input == "b":
            print(f"your account balance is ${user_balance}")
            break
        if user_input == "q":
            break
        else :
            print("invalid input! please try again later ")
    else:
        password_try = password_try - 1
else:
    print("please try again later")   

    
