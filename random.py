import random
lucky_number=int(random.randint(0,9))
print(lucky_number)
playing_amount=int(input("Enter the amount you want to play with : "))
no_of_chances = 3
while no_of_chances > 0:
    selected_number=int(input("please choose a number between 0 to 9 :"))
    if selected_number != lucky_number:
        no_of_chances = no_of_chances-1
    else:
        if no_of_chances == 3:
            print(f"hurray you won\n your winning amount is {playing_amount*3*3}")
            break
        elif no_of_chances == 2:
            print(f"hurray you won\n your winning amount is {playing_amount*3}")
            break
        else:
            print(f"hurray you won\n your winning amount is {playing_amount*0.5}")
            break
else:
    print("you lost all of your chances.")




