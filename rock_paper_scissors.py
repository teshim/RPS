import random

DEFEATED_BY = {'rock' : 'scissors', 'scissors' : 'paper', 'paper' : 'rock'}

def main():
    print("Hello! Welcome to Rock Paper Scissors: CS45 edition!")
    print("This is a two player game, with rules as follows:")
    print("Each player secretly selects one out of 'rock', 'paper', and 'scissors'")
    print("Then, both players reveal their choice simultaneously, and a winner is decided.")
    print("Rock beats scissors, scissors beats paper, and paper beats rock.")
    print("If both players make the same selection, then it's a tie. Let's play!\n")

    while True:
        userMove = input("Make your selection (rock, paper, or scissors): ")
        print("You selected " + userMove + ".")
        computerMove = random.choice(['rock', 'paper', 'scissors'])
        print("The computer selected " + computerMove + ".")
        if computerMove == DEFEATED_BY[userMove]:
            print("You win!")
            break
        elif userMove == DEFEATED_BY[computerMove]:
            print("The computer wins!")
            break
        print("It's a tie - play another round!\n")

if __name__ == "__main__":
    main()
