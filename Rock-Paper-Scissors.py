import random as r
import os
import time

#name of the player
name = input("Enter Your Name : ")
#for computer
choose = ['ROCK', 'PAPER', 'SCISSOR']



def play():
    os.system("clear")
    print(f"WELCOME {name}!")
    valid = []


    while len(valid) != 5:
        print("----------------------------------------")
        user = input("Enter ROCK, PAPER, SCISSOR : ").strip().upper()
        computer = r.choice(choose)
        print("----------------------------------------")


        if user == computer:               
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'computer: {computer}\n')
                print("IT's A TIE!\n")


        elif user == 'ROCK' and computer == 'SCISSOR' or user == 'S' and computer == 'SCISSOR':
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                valid.append(1)
                print(f'{name.upper()} , WON!' if user == 'R' else f'COMPUTER WON!\n')


        elif user == 'SCISSOR' and computer == 'PAPER' or user == 'PAPER' and computer == 'SCISSORP':
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                valid.append(1)
                print(f'{name.upper()} , WON!' if user == 'R' else f'COMPUTER WON!\n')


        elif user == 'PAPER' and computer == 'ROCK' or user == 'ROCK' and computer == 'PAPER':
                time.sleep(1)
                print(f'{name}: {user}')
                print(f'Computer: {computer}\n')
                valid.append(1)
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
