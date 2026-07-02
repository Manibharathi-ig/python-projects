import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock , Paper , scissors or Q to quit :").lower()
    if user_input == "q":
        break
    if user_input  not in options:
        continue

    random_number = random.randint(0,2)
    # rock:0 , paper:1 , scissors:2
    computer_picks = options[random_number]
    print("computer picked" , computer_picks  , "." )

    if user_input == computer_picks:
        print("Its a tie!")

    elif user_input == "rock" and computer_picks == "scissors":
        print("you got it!")
        user_wins +=1
        

    elif user_input == "paper" and computer_picks == "rock":
        print("you got it!")
        user_wins +=1
        

    elif user_input == "scissors" and computer_picks == "paper":
        print("you got it!")
        user_wins +=1
        

    else:
        print("you lost it!")
        computer_wins +=1

print("you won" , user_wins , "wins")
print("computer won" , computer_wins , "wins")
print("Goodbye")


    

