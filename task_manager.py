# Task Manager Application

# Initialize an empty list to store tasks
tasks = []
# Initialize a variable to track the last assigned sequence number
last_sequence_number = 0
# Initialize an empty list to store deleted sequence numbers
deleted_sequence_numbers = []

# Function to add a new task
def add_task(task_name):
    global last_sequence_number
    if deleted_sequence_numbers:
        sequence_number = deleted_sequence_numbers.pop(0)
    else:
        last_sequence_number += 1
        sequence_number = last_sequence_number
    new_task = {"Sequence Number": sequence_number, "Task Name": task_name, "Status": "Pending"}
    tasks.append(new_task)
    print("New task added successfully.")

# Function to mark a task as completed
def complete_task(sequence_number):
    for task in tasks:
        if task["Sequence Number"] == sequence_number:
            task["Status"] = "Completed"
            print("Task marked as completed.")
            return
    print("Task not found.")

# Function to delete a task
def delete_task(sequence_number):
    for task in tasks:
        if task["Sequence Number"] == sequence_number:
            tasks.remove(task)
            deleted_sequence_numbers.append(sequence_number)
            print("Task deleted.")
            return
    print("Task not found.")

# Function to list completed tasks
def list_completed_tasks():
    print("Completed Tasks:")
    for task in sorted(tasks, key=lambda x: x["Sequence Number"]):
        if task["Status"] == "Completed":
            print(f"Sequence Number: {task['Sequence Number']}, Task Name: {task['Task Name']}")

# Function to list all tasks with their status
def list_all_tasks():
    print("All Tasks:")
    for task in sorted(tasks, key=lambda x: x["Sequence Number"]):
        print(f"Sequence Number: {task['Sequence Number']}, Task Name: {task['Task Name']}, Status: {task['Status']}")

# Main function
def main():
    while True:
        print("\nOperations:")
        print("1. Add a new task")
        print("2. Complete a task")
        print("3. Delete a task")
        print("4. List completed tasks")
        print("5. List all tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == "2":
            sequence_number = int(input("Enter the sequence number of the task to mark as completed: "))
            complete_task(sequence_number)
        elif choice == "3":
            sequence_number = int(input("Enter the sequence number of the task to delete: "))
            delete_task(sequence_number)
        elif choice == "4":
            list_completed_tasks()
        elif choice == "5":
            list_all_tasks()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
