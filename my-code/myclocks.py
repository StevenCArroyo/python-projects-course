
import time
from datetime import datetime
import os
import threading
from zoneinfo import ZoneInfo

def clear_screen():
	os.system('clear')

#wait for user to hit enter
def input_thread(stop_event):
	input()
	stop_event.set()


def main():

	#setup timezones
	time_zones = {
	'1': ('Eastern Time', 'America/New_York'),
	'2': ('Central Time', 'America/Chicago'),
	'3': ('Pacific Time', 'America/Los_Angeles')
	}

	#promt for timezone
	print("Select a timezone:  ")
	#loop through dictionary, where value is a tuple
	for key, (name, _) in time_zones.items():
		print(f"{key}. {name} : ")

	#assign selection to variable
	choice = input("Enter the number of your choice: ").strip()

	#error handling for choice
	if choice not in time_zones:
		print("Invalid choice. Defaulting to Eastern Time.")
		tz_name = "America/New_York"
		tz_display_name = "Eastern Time"
	else:
		tz_display_name, tz_name = time_zones[choice]




	#create an event to signal when to stop the clock
	stop_event = threading.Event()

	#start the input thread
	thread = threading.Thread(target=input_thread, args=(stop_event, ))
	thread.daemon = True
	thread.start()

	while not stop_event.is_set():
		clear_screen()
		#current time
		#current_time = time.strftime("%H:%M:%S")
		current_time = datetime.now(ZoneInfo(tz_name)).strftime("%H:%M:%S")
		print(f"Current time: {current_time} - {tz_display_name}")
		#prompt user to stop clock
		print("Press enter to stop the clock")
		#run loop once per second
		time.sleep(1)

	#print end message
	print("Clock stopped")



#main function
main()