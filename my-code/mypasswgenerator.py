
import os
import random
import string


os.system("clear")


#validate user's password
def validate_password(password):
	#check password rules
	if len(password) < 8:
		return False, "Password too short"
	if not any(char.isdigit() for char in password):
		return False, "1 digit required"
	if not any(char.islower() for char in password):
		return False, "must contain 1 lowercase letter"
	if not any(char.isupper() for char in password):
		return False, "must contain 1 uppercase letter"
	if not any(char in string.punctuation for char in password):
		return False, "must contain 1 special character"
	#return True is all rules met
	return True, "Password accepted"

#generate password
def generate_password(length):
	while True:
		#ensure meets rules
		password = [
			#one lowercase
			random.choice(string.ascii_lowercase),
			#one uppercase
			random.choice(string.ascii_uppercase),
			#one digit
			random.choice(string.digits),
			#one special char
			random.choice(string.punctuation),
		]
		#fill the rest of password with random chars from all sets
		#get remaining char count
		remaining_length = length - 4
		password += random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=remaining_length)
		#shuffle list
		random.shuffle(password)
		#convert list to string
		password = ''.join(password)

		#validate password (it already is!)
		is_valid, message = validate_password(password)
		if is_valid:
			return password




#promt user
def password_generator():
	while True:
		try:
			#get password length
			length = int(input("Enter the password length (min 8):  "))
			if length < 8:
				print("Password length must be at lease 8 characters.")
				continue
			break
		except ValueError:
			print("Invalid input, enter a number.")

	#generate password
	password = generate_password(length)
	print(f"Generated password: ", password)

#run
password_generator()





