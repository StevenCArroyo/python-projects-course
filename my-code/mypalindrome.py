import os

os.system("clear")

def is_palindrome(string):
	#remove spaces and convert to lowercase, strip notation
	'''
	cleaned_string = ''
	#loop through user input
	for character in string:
		#check if character is alphanumeric
		if character.isalnum():
			cleaned_string += character.lower()
	#print(cleaned_string)
	#check if palindrome
	return cleaned_string == cleaned_string[::-1]
	'''
	#Shorthand for the above code
	cleaned_string = ''.join(character.lower() for character in string if character.isalnum())
	return cleaned_string == cleaned_string[::-1]

#user input
user_input = input("Enter a word or phrase to check if palindrome:  ")

#slice = [start:end:step]
#user_input = user_input[::-1]
if is_palindrome(user_input):
	print(f"{user_input} is a palindrome.")
else:
	print(f"{user_input} is not a palindrome.")	
