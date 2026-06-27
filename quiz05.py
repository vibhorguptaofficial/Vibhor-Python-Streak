import random

options = ["Snake", "Water", "Gun"]

Computer_choice =  random.choice(options)

print("Welcome to the game")
user_choice = input("Enter your choice(Snake, Water, Gun): ").capitalize()



print(f"Computer Choice is {Computer_choice}")
print(f"Your choice is {user_choice}")  


if Computer_choice == "Snake":
    if  user_choice == "Water":
        print("You have loss")
    elif user_choice == "Snake":
        print("Your match is draw")
    elif user_choice == "Gun":
        print("you are win")
    else:
        print("invalid choice ! please again choose")


if Computer_choice == "Water":
    if  user_choice == "Gun":
        print("You have loss")
    elif user_choice == "Water":
        print("Your match is draw")
    elif user_choice == "Snake":
        print("you are win")
    else:
        print("invalid choice ! please again choose")


if Computer_choice == "Gun":
    if  user_choice == "Snake":
        print("You have loss")
    elif user_choice == "Gun":
        print("Your match is draw")
    elif user_choice == "Water":
        print("you are win")
    else:
        print("invalid choice ! please again choose")



