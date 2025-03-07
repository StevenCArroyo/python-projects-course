
from tkinter import *
import os
import random


#functions

def reset_game(guess_entry,result_label,submit_button,play_again_button,state):
	#random between 1-10
	state['number_to_guess']  = (random.randint(1,10))
	#set number of guesses to 0
	state['number_of_guesses'] = 0
	#Delete result label
	result_label.config(state=NORMAL)
	#clear entry box
	guess_entry.delete(0,END)
	#Set the submit button to normal
	submit_button.config(state=NORMAL)
	#Hide play again button
	play_again_button.pack_forget()


	#On start reset game
	reset_game(guess_entry,result_label,submit_button,play_again_button,state)

	#start the app
	root.mainloop()

def check_guess(guess_entry,result_label,submit_button,play_again_button,state):
	#Try/except block
	try:
		guess = int(guess_entry.get())
		state['number_of_guesses'] += 1
		#create logic to check if guess is correct
		if guess < state['number_to_guess']:
			result_label.config(text="Your guess is too low. Try again!")
		elif guess > state['number_to_guess']:
			result_label.config(text="Your guess is to high. Try again!")
		else:
			result_label.config(text=f"Correct, the number was {state['number_to_guess']} and you guessed it in {state['number_of_guesses']} tries.")
			#disable the guess button
			submit_button.config(state=DISABLED)
			#enble play again button
			play_again_button.pack()

	except ValueError:
		result_label.config(test="Invalid input! Please enter a number. ")
		return
		print(e)

def setup_gui():
	#create window
	root = Tk()
	# add title
	root.title("Guessing Game")
	#set size of window
	root.geometry('500x350')

	#set the game state
	state = {'number_to_guess':(random.randint(1,10)), 'number_of_guesses':0}


	#create label top
	instruction_label = Label(root, text="Guess a nuber between 1 and 10", font=("Helvetica", 18))
	#20 pixels above and below label
	instruction_label.pack(pady=20)
	
	#create enty box
	guess_entry = Entry(root,font=("Helvetica", 18))
	guess_entry.pack(pady=10)

	#create another label
	result_label = Label(root, text="")
	result_label.pack(pady=20)
	
	#create buttons
	submit_button = Button(root, text="Submit Guess", command=lambda: check_guess(guess_entry,result_label,submit_button,play_again_button,state))
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?", command=lambda: reset_game(guess_entry,result_label,submit_button,play_again_button,state))
	play_again_button.pack()
	#hide button until it's time to play again
	play_again_button.pack_forget()

	#start the app
	root.mainloop()

#call main function
setup_gui()