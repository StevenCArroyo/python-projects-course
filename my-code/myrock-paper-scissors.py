
import sys
import random

answ = input("Chose rock, paper, or scissors:  [r, p, s]: ")

if answ == "r":
	my_choice = "rock"
elif answ == "p":
	my_choice = "paper"
elif answ == "s":
	my_choice = "scissors"
else:
	print("unknown option")
	sys.exit()

print(f"You entered: ", my_choice)

options = ["rock", "paper", "scissors"]
comp_choice = random.choice(options)

print(f"Computer selected: ", comp_choice)
#check if you win
#rock beats scissors
if my_choice == "rock" and comp_choice == "scissors":
	print(f"You win: {my_choice} beats {comp_choice}")
#paper beats rock
elif my_choice == "paper" and comp_choice == "rock":
	print(f"You win: {my_choice} beats {comp_choice}")
#scissors beats paper
elif my_choice == "scissors" and comp_choice == "paper":
	print(f"You win: {my_choice} beats {comp_choice}")
#check if computer wins
#rock beats scissors
if comp_choice == "rock" and my_choice == "scissors":
	print(f"You lose: {comp_choice} beats {my_choice}")
#paper beats rock
elif comp_choice == "paper" and my_choice == "rock":
	print(f"You lose: {comp_choice} beats {my_choice}")
#scissors beats paper
elif comp_choice == "scissors" and my_choice == "paper":
	print(f"You lose: {comp_choice} beats {my_choice}")
#tie
elif my_choice == comp_choice:
	print(f"Tie game")