
import os
from pynput import keyboard

os.system("clear")

def on_press(key):
	try:
		#check for q
		if key.char == "q":
			print("Exiting")
			return False
	except AttributeError:
		pass

	#check for arrow keys
	if key == keyboard.Key.up:
		print("Up")
	elif key == keyboard.Key.down:
		print("Down")
	elif key == keyboard.Key.left:
		print("left")
	elif key == keyboard.Key.right:
		print("right")



#prompt user
print("Press arrow keys or q to exit ")



#create and start a keyboard listner
#create listener object, for keyboard events
with keyboard.Listener(on_press=on_press) as listener: 
	#start listener and wait for it to finish
	listener.join()

