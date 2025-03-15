
import os


os.system("clear")

#add task to list where tasks is a list of dictionaries
'''
tasks = [
	{"task": "wash the car", "completed": False},
	{"task": "take a nap", "completed": True}
]
'''
def add_task(tasks, task):
	tasks.append({"task": task, "completed": False})
	print(f"Task {task} has been added.")
	return tasks 

#view tasks
def view_tasks(tasks):
	if not tasks:
		print("No tasks in list.")
	else:
		print("\nTodo list: ")
		#enumerate list of tasks print starting at 1
		for idx, task_info in enumerate(tasks, 1):
			status = "Done" if task_info["completed"] else "Not Done"
			print(f'{idx}. {task_info["task"]} - {status}')
		#print(tasks)
	print()


#remove tasks
def remove_task(tasks, task_index):
	if 0 <= task_index < len(tasks):
		remove_task = tasks.pop(task_index)
		print(f"Removed task: {remove_task['task']}")
	else:
		print("Invalid task number.")
	return tasks
	

#mark task complete
def mark_task_completed(tasks, task_index):
	if 0 <= task_index < len(tasks):
		#update todo item
		tasks[task_index]["completed"] = True
		print(f'Task "{tasks[task_index]["task"]} marked as completed." ')
	else:
		print("Invalid task number.")
	return tasks



#main todo function
def to_do_list_app():
	#create list of dictionaries for todo's
	tasks = []

	while True:
		os.system("clear")

		print("\n--- Todo list menu ---")
		print("1. Add task")
		print("2. View tasks")
		print("3. Remove task")
		print("4. Mark task completed")
		print("5. Exit")

		choice = input("Chose and option: ")

		if choice == '1':
			task = input("Enter the task: ")
			tasks = add_task(tasks, task)
			#tell user to hit enter
			input("\nPress enter to continue:  ")
		elif choice == '2':
			view_tasks(tasks)
			#tell user to hit enter
			input("\nPress enter to continue:  ")
		elif choice == '3':
			if tasks:
				view_tasks(tasks) #print todo list
				task_index = int(input("Enter task number to remove: ")) -1
				tasks = remove_task(tasks, task_index)
			else:
				print("No tasks in list!")
			#tell user to hit enter
			input("\nPress enter to continue:  ")
		elif choice == '4':
			if tasks:
				view_tasks(tasks) #print todo list
				task_index = int(input("Enter task number to mark complete: ")) -1
				tasks = mark_task_completed(tasks, task_index)
			else:
				print("No tasks in list!")
			#tell user to hit enter
			input("\nPress enter to continue:  ")
		elif choice == '5':
			break
		else:
			print("Invalid option.")
			#tell user to hit enter
			input("\nPress enter to continue:  ")

	

#run app
to_do_list_app()
