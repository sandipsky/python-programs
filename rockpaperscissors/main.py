import random
game = True
print("###Rock, paper and Scissors game by SandipSky##")
print("Your choices are rock(1), paper(2), scissors(3)")



def playgame():
    win = None
    player_point=0
    computer_point=0
    inp = (input("Enter your choice: ")).lower()
    options = ['rock', 'paper', 'scissors', '1', '2', '3']
    sy = random.choice(options)
    if inp in options:
        print("Your choice: " + inp)
        print("Computer choice: "+ sy)
        if (inp == 'rock' or inp == '1') and (sy == 'scissors' or sy =='3'):
            win = True
        elif (inp == 'paper' or inp =='2') and (sy == 'rock' or sy == '1'):
            win = True
        elif (inp == 'scissors' or inp == '3') and (sy == 'paper' or sy == '2'):
            win = True
        elif inp == sy:
            print("Its a tie.")
        else:
            print("Sorry! You lost")
            computer_point += 1

        if win:
            print("Congrats! You won")
            player_point += 1
    else:
        print("Please enter a valid option")

    print(f"Computer point: {computer_point}")
    print(f"Player point: {player_point}")


while(game):
    playgame()
    x = input(("Do u want to play again?(Y/n) ")).lower()
    if x == 'y':
        game = True
    else:
        game = False



