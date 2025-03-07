
from tkinter import *
import os
import random

#Initialize game start variables (global)

#number_to_guess = None
#random between 1-10
number_to_guess  = (random.randint(1,10))
number_of_guesses = 0


#functions

def reset_game():
	#set global varialbes
	global number_to_guess, number_of_guesses
	#random between 1-10
	number_to_guess  = (random.randint(1,10))
	#set number of guesses to 0
	number_of_guesses = 0
	#Delete result label
	result_label.config(state=NORMAL)
	#clear entry box
	guess_entry.delete(0,END)
	#Set the submit button to normal
	submit_button.config(state=NORMAL)
	#Hide play again button
	play_again_button.pack_forget()


	#On start reset game
	reset_game()

	#start the app
	root.mainloop()

	

def check_guess():
	
	global number_of_guesses
	
	#Try/except block
	try:
		guess = int(guess_entry.get())
		number_of_guesses += 1
		#create logic to check if guess is correct
		if guess < number_to_guess:
			result_label.config(text="Your guess is too low. Try again!")
		elif guess > number_to_guess:
			result_label.config(text="Your guess is to high. Try again!")
		else:
			result_label.config(text=f"Correct, the number was {number_to_guess} and you guessed it in {number_of_guesses} tries.")
			#disable the guess button
			submit_button.config(state=DISABLED)
			#enble play again button
			play_again_button.pack()

	except ValueError:
		result_label.config(test="Invalid input! Please enter a number. ")
		return
		print(e)

def setup_gui():
	#make all widgets global
	global result_label, guess_entry, submit_button, play_again_button
	#create window
	root = Tk()
	# add title
	root.title("Guessing Game")
	#set size of window
	root.geometry('500x350')

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
	submit_button = Button(root, text="Submit Guess", command=check_guess)
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?", command=reset_game)
	play_again_button.pack()
	#hide button until it's time to play again
	play_again_button.pack_forget()


	#start the app
	root.mainloop()

#call main function
setup_gui()