import random
Name = input("Type your name: ")
print("Welcome" , Name , "to this adventure !")


answer = input("you are on a dirt road , it has come to an end and you can go left or right .which way would you like to go? ").lower()

if answer == "left":
    answer = input("you came to a river , you can walk around it or swim across? Type walk or swim ")
    if answer == "swim":
        print("you swam across and were eaten by a aligator")
    elif answer == "walk":
        print("you walked for miles , ran out of water and you lost the game")
    else:
        print("not a valid answer. you lose! ")

elif answer == "right":
    answer = input("you come to a bridge , it looks woobly , do you want to cross it or head back? Type cross/back").lower()
    if answer == "back":
        print("you go back and lose")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger , do you want to talk to them ? type yes /no").lower()

        if answer == "yes":
            print("you talk to the stranger and they give you gold." , Name , " you WIN! ")
        elif answer == "no":
            print("you ignore the stranger and they offended you and you lose")
        else:
            print("not a valid option. you lose.")
    else:
        print("not a valid option. you lose.")
else:
    print("not a valid option. you lose! ")



