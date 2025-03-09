import os
import random

os.system("clear")

def get_computer_choice():
	#computer select rps
	choices = ["rock", "paper", "scissors"]
	return random.choice(choices)

def get_user_choice():
	choices = {1:"rock", 2:"paper", 3:"scissors"}
	try:
		user_input = int(input("Enter 1:rock, 2:paper, 3:scissors:  "))
		if user_input in choices:
			return choices[user_input]
		else:
			print("Invalid choice try again")
			return get_user_choice()
	except ValueError:
		print("Enter a number between 1 and 3:  ")
		return get_user_choice()

def determine_winner(user_choice, computer_choice):
	#tie
	if user_choice == computer_choice:
		return "TIE"
	elif (user_choice == "rock" and computer_choice == "scissors") or \
		 (user_choice == "scissors" and computer_choice == "paper") or \
		 (user_choice == "paper" and computer_choice == "rock"):
		return "You win"
	else:
		return "You lose"

def play_again():
	while True:
		user_input = input("play again?: y or n:  ").lower()
		if user_input in ['y', 'n']:
			#if y is in list, return y, comparison, is user input y which 
			#equals True and returns True to play_game() function which
			#means play again
			return user_input == 'y'  #if n then returns False to play_game()
		else:
			print("invalid input")


#set up the game
def play_game():
	while True:
		os.system("clear")
		user_choice = get_user_choice()
		#get computer choice
		computer_choice = get_computer_choice()
		#output choices
		print(f"you chose {user_choice}")
		print(f"Computer chose {computer_choice}")

		#determine winner
		result = determine_winner(user_choice, computer_choice)
		print(result)

		#end game
		if not play_again():
			print("bye")
			#break out of while True above
			break

#play the game
play_game()



