import random as r

#name of the player
name = input("Enter Your Name : ")
#for computer
choose = ['ROCK', 'PAPER', 'SCISSOR']


def play():
    for i in range(5):
        print("----------------------------------------")
        user = input("Enter ROCK, PAPER, SCISSOR : ").strip().upper()
        computer = r.choice(choose)
        print("----------------------------------------")

        if user == computer:
                print(f'{name}: {user}')
                print(f'computer: {computer}\n')
                print("IT's A TIE!\n")


        elif user == 'ROCK' and computer == 'SCISSOR' or user == 'S' and computer == 'SCISSOR':
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                print(f'{name.upper()} , WON!' if user == 'R' else f'COMPUTER WON!\n')


        elif user == 'SCISSOR' and computer == 'PAPER' or user == 'PAPER' and computer == 'SCISSORP':
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                print(f'{name.upper()} , WON!' if user == 'R' else f'COMPUTER WON!\n')


        elif user == 'PAPER' and computer == 'ROCK' or user == 'ROCK' and computer == 'PAPER':
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                print(f'{name.upper()} , WON!' if user == 'R' else f'COMPUTER WON!\n')


        else:
                print("INVALID INPUT! TRY AGAIN...\n")


#intial
play()

while True:

    play_again = input("Want To Play Again? (y/n) : ").strip().upper()

    if play_again == 'Y':
        play()
    else:
        break
