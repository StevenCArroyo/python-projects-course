
import os
import string

os.system("clear")


#print out special chars
#print(string.punctuation)

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

#print out password rules
def show_password_rules():
	print("Password rules:")
	print("must be 8 chars long")
	print("must contain 1 digit")
	print("must contain one lowercase letter")
	print("must contain one uppercase letter")
	print("must contain 1 special character")
	print()


def password_validator():
	#passwd rules
	show_password_rules()
	#prompt user for their password
	password = input("Please enter your password:  ")

	#validate password
	is_valid, message = validate_password(password)
	#return result
	if is_valid:
		print("Success: ", message)
	else:
		print("Failed: ", message)


password_validator()