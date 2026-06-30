print("welcome to my game!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("okay , let's go :) ")

score = 0

answer = input("What does csv stands for? ")
if answer.lower() == "comma seperated values":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("Which language is mostly used in data science ")
if answer.lower() == "python":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("Which library is mostly used for data analysis ")
if answer.lower() == "pandas":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("Which library is mostly used for numerical operations ")
if answer.lower() == "numpy":
    print("correct")
    score +=1
else:
    print("incorrect")

answer = input("Which library is mostly used for data visulaization ")
if answer.lower() == "matplotlib":
    score +=1
    print("correct")
else:
    print("incorrect")

print("you got" + str(score) + "questions correct")
print("you got" + str((score/5) * 100) + "%" )