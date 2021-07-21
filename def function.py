import random
user_guess = input("guess a no. between 1 to 6 :")
def rolling_dice():
    random_number = str(random.randit(1,6))
    if user_guess == random_number:
        print(f"you won!")
    else: 
        print(f"better luck next time!\nDo you want to play again?")


rolling_dice