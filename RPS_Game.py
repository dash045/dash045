import random

comp_wins = 0
player_wins = 0

def Player_Choice():
    user_choice = input("Choose Rock, Paper, Scissors: ")
    if user_choice in ["Rock","rock","r","R"]:
        user_choice ="r"
    elif user_choice in ["Paper","paper","p","P"]:
        user_choice ="p"
    elif user_choice in ["Scissors","scissors","s","S"]:
        user_choice ="s"
    else:
        print("I don't understand the choice, try again!")
        Player_Choice()
    return user_choice

def Computer_Choice():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice= "p"
    elif comp_choice== 3:
        comp_choice= "s"
    return comp_choice

while True:
    print("")
    user_choice = Player_Choice()
    comp_choice = Computer_Choice()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose ROCK. The computer chose ROCK. Game Tied!")
        elif comp_choice == "p":
            print("You chose ROCK. The computer chose PAPER. You Lose!")
            comp_wins +=1
        elif comp_choice == "s":
            print("You chose ROCK. The computer chose SCISSOR. You Win!")
            player_wins +=1
    elif user_choice == "p":
        if comp_choice == "p":
            print("You chose PAPER. The computer chose PAPER. Game Tied!")
        elif comp_choice == "s":
            print("You chose PAPER. The computer chose SCISSOR. You Lose!")
            comp_wins +=1
        elif comp_choice == "r":
            print("You chose PAPER. The computer chose ROCK. You Win!")
            player_wins +=1
    elif user_choice == "s":
        if comp_choice == "s":
            print("You chose SCISSOR. The computer chose SCISSOR. Game Tied!")
        elif comp_choice == "r":
            print("You chose SCISSOR. The computer chose ROCK. You Lose!")
            comp_wins +=1
        elif comp_choice == "p":
            print("You chose SCISSOR. The computer chose PAPER. You Win!")
            player_wins +=1

    print("")
    print("Players wins: " + str(player_wins))
    print("Computer wins: "+ str(comp_wins))
    print("")

    user_choice = input("Do you want to player again?, (Y/N)")
    if user_choice in ["Y", "y","yes","YES"]:
        pass
    elif user_choice in ["N","n","no","NO"]:
        print("Thank you for playing!")
        break
    else:
        break

