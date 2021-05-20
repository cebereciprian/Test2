import random
# My first Repository
# Rock-Paper-Scissors-Lizard-Spock
#aasrrsa

person = input("Enter your name: ")
print("Hello!!! Welcome to my game", person)


def play():

    print("Welcome to Rock - Paper - Scissors - Lizard - Spock")
    print("The rules of the game are: ")
    print("Scissors cuts Paper \t\t\t\t Scissors decapitates Lizard")
    print("Paper covers Rock \t\t\t\t Lizard eats Paper  ")
    print("Rock crushes Lizard \t\t\t\t Paper disproves Spock")
    print("Lizard poisons Spock \t\t\t\t Spock vaporises Rock")
    print("Spock smashes Scissors \t\t\t\t (and as it always has) Rock crushes Scissors")

    choice = input(
        "Let's have fun. Please enter your choice (Rock / Paper / Scissors / Lizard / Spock): ")

    game = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    computer = random.choice(game)

    print(f"\nYour choice is {choice} vs Computer's choice is {computer}. \n")

    if choice == computer:
        print(input("it was a tie !!! Please make another choice: "))
    elif choice == "Scissors":
        if computer == ("Paper", "Lizard"):
            print("You win!!!")
        else:
            print("You loose!!!")
    elif choice == "Rock":
        if computer == ("Lizard", "Scissors"):
            print("You win!!!")
        else:
            print("You loose")
    elif choice == "Paper":
        if computer == ("Rock", "Spock"):
            print("You win!!!")
        else:
            print("You loose!!!")
    elif choice == "Spock":
        if computer == ("Scissors", "Rock"):
            print("You win!!!")
        else:
            print("You loose!")
    elif choice == "Lizard":
        if computer == ("Spock", "Paper"):
            print("You win!!!")
        else:
            ("You loose!!!")


while True:
    answer = input("Do you wan't to play ? (Y/N) --------->")
    if answer == "Y":
        play()
    elif answer == "N":
        print("Thanks for playing!!!")
        break
    else:
        print("I don't understand the answer")


# commit