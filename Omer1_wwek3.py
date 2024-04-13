tasks = []

def add_task(task_name):
    tasks.append({'task_name': task_name, 'status': 'Pending'})

def complete_task(task_name):
    task_found = False
    print(tasks)  # Debugging print statement
    for task in tasks:
        if task['task_name'] == task_name:
            task['status'] = 'Completed'
            print(f"Task {task_name} marked as completed.")
            task_found = True
            break
    if not task_found:
        print("Task not found.")

def delete_task(task_name):
    task_found = False
    for task in tasks:
        if task['task_name'] == task_name:
            task['status'] = 'Deleted'
            print(f"Task {task_name} marked as deleted.")
            task_found = True
            break
    if not task_found:
        print("Task not found.")

def list_completed_tasks():
    completed_tasks = [task['task_name'] for task in tasks if task['status'] == 'Completed']
    if completed_tasks:
        print("Completed Tasks:")
        for task_name in completed_tasks:
            print(task_name)
    else:
        print("No completed tasks found.")

def list_all_tasks():
    if tasks:
        print("All Tasks:")
        for task in tasks:
            print(task['task_name'], "-", task['status'])
    else:
        print("No tasks found.")

while True:
    print("1. Add a new task")
    print("2. Complete a task")
    print("3. Delete a task")
    print("4. List completed tasks")
    print("5. List all tasks with status")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task_name = input("Enter task name: ")
        add_task(task_name)
        print(f"Task '{task_name}' added successfully.")
    elif choice == '2':
        task_name = input("Enter task name to mark as completed: ")
        complete_task(task_name)
    elif choice == '3':
        task_name = input("Enter task name to delete: ")
        delete_task(task_name)
    elif choice == '4':
        list_completed_tasks()
    elif choice == '5':
        list_all_tasks()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
