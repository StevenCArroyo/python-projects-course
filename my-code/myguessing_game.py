
import os
import random

#functions

def play_again():
	again = input("play again? y/n ")
	if again == "y":
		game()
	else:
		print("Thanks for playing")
		return

def game():
	
	#number of guesses
	number_of_guesses = 0
	correct = False

	os.system("clear")

	#random between 1-10
	#print(random.randint(1,10))
	number_to_guess  = (random.randint(1,10))

	#user input
	print("Guess number between 1 & 10")
	while correct == False:

		#Try/except block
		try:
			guess = int(input("Enter your guess:  "))
			print(f"You guessed: ", guess)

		except Exception as e:
			print("Somtehing is wrong, game over")
			return
			print(e)
		#create logic to check if guess is correct
		if guess < number_to_guess:
			print("Your guess is too low")
			number_of_guesses += 1
		elif guess > number_to_guess:
			print("Your guess is too high")
			number_of_guesses += 1
		elif guess == number_to_guess:
			number_of_guesses += 1
			print(f"Correct, the number was {number_to_guess} and you guessed it in {number_of_guesses} tries.")
			correct = True
			#run play again function
			play_again()


#call game
game()
