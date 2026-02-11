import random as r
import os
import time

# clearing the screen to look visually better
os.system("clear")

#name of the player
name = input("Enter Your Name : ").strip().upper()

#for computer
hand = ['ROCK', 'PAPER', 'SCISSOR']


def play():
    os.system("clear")
    print(f"WELCOME {name.upper()}!")
    round = []

    while len(round) != 5:
        print("----------------------------------------")
        user = input("Enter ROCK, PAPER, SCISSOR : ").strip().upper()
        computer = r.choice(hand)
        print("----------------------------------------")


        if user == computer:               
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'computer: {computer}\n')
                print("IT's A TIE!\n")


        elif user == 'ROCK' and computer == 'SCISSOR' or user == 'SCISSOR' and computer == 'ROCK':
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                print(f'{name} , WON!' if user == 'ROCK' and computer=='SCISSOR' else f'COMPUTER WON!\n')
                round.append(1)


        elif user == 'SCISSOR' and computer == 'PAPER' or user == 'PAPER' and computer == 'SCISSOR':
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                print(f'{name} , WON!' if user == 'SCISSOR' and computer=='PAPER' else f'COMPUTER WON!\n')
                round.append(1)


        elif user == 'PAPER' and computer == 'ROCK' or user == 'ROCK' and computer == 'PAPER':
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                print(f'{name} , WON!' if user == 'PAPER' and computer=='ROCK' else f'COMPUTER WON!\n')
                round.append(1)


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
