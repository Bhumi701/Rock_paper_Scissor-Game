import random
tools = ["Paper", "Rock", "Scissor"]

You = input("Enter your move = Paper, Rock, Scissor:")
Me = random.choice(tools)

print(f"You = {You},Me = {Me}")

if(You == Me):
    print("We chooses SAME: Match Tie")
elif(You == "Rock"):
    if(Me == "Paper"):
        print("Paper covers Rock = I win")
    else:
        print("Rock smashes Scissors = You win")
elif(You == "Paper"):
    if(Me == "Scissor"):
        print("Scissor cuts paper = I win")
    else:
        print("Paper covers Rock = You win")
elif(You == "Scissor"):
    if(Me == "Rock"):
        print("Rock smashes Scissor = I win")
    else:
        print("Scissor cuts Paper = You win")
else:
    pass
