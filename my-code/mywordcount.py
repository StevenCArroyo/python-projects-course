
import os



os.system("clear")


#function to count words
def count_words(sentence):
	#split sentence into a list
	words = sentence.split()

	#len of list
	return len(words)


#function to count the number of characters
def count_characters_with_spaces(sentence):
	#use len 
	return len(sentence)

#function to count the number of chars without spaces
def count_characters_without_spaces(sentence):
	#remove spaces
	return len(sentence.replace(" ", ""))


#main
def word_count_program():
	#prompt for input
	sentence = input("Enter a sentence.: ")

	if sentence:
		#get word count and characther counts
		word_count = count_words(sentence)
		char_count_with_spaces = count_characters_with_spaces(sentence)
		char_count_without_spaces = count_characters_without_spaces(sentence)
		
		#print results
		print(f'Word count: {word_count}')

		print(f'Charcaters with spaces:  {char_count_with_spaces}')

		print(f'Charcaters without spaces:  {char_count_without_spaces}')

	else:
		print("Not a sentence.")

word_count_program()


