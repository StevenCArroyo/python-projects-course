
import os
import random



os.system("clear")

#create list of words
word_list = ['python', 'javascript', 'ruby', 'perl', 'developer', 'coder', 'hangman', 'function', 'syntax']

#select random word from word_list
def get_random_word():
	return random.choice(word_list)

#print(get_random_word())


#display the current state of the guessed word
def display_word(word, guessed_letters):
	#for each letter in word, put the letter in guessed_letters
	#and print it to the screen. otherwise print "_" meaning letter
	#hasn't been guessed yet
	#join with spaces in between "_"
	return ' '.join([letter if letter in guessed_letters else "_" for letter in word])

#main game logic
def play_hangman():
	#get random word
	word = get_random_word()
	#get lentgh of word
	word_length = len(word)


	#keep track of guessed letters and incorrect guesses
	#set, can add to set only, no dups allowed (prevents same guesses)
	guessed_letters = set()
	incorrect_guesses = set()
	lives = 6 #number of incorrect guesses allowed

	#prompt for letter
	print("Welcome to hangman")
	print(f"The word hs {word_length} letters.")

	#main game loop
	while lives > 0:
		#display current word status
		print("\n" + display_word(word, guessed_letters))
		print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
		print(f"Lives remaining {lives}")

		#prompt user for guess
		guess = input("Guess a letter: ").lower()

		#validate the guessed letter
		if len(guess) != 1 or not guess.isalpha():
			os.system("clear")
			print("Invalid input, enter a single letter.")
			continue

		#check if the letter has been guessed
		if guess in guessed_letters or guess in incorrect_guesses:
			os.system("clear")
			print(f"You already guessed {guess}. Try again.")
			continue

		#check if guess is correct
		if guess in word:
			os.system("clear")
			guessed_letters.add(guess)
			print(f"Good guess. {guess} is in the word.")
		else:
			os.system("clear")
			incorrect_guesses.add(guess)
			#remove a live
			lives -= 1
			print(f"Wrong guess. {guess} is not in the word.")

		#check if player guessed the work
		if all(letter in guessed_letters for letter in word):
			print(f"\nCongratulations! You guess the word: {word}.")
			break



	#if player runs out of lives
	if lives == 0:
		print(f"\nYou ran out of lives. The word was, {word}.")





play_hangman()




