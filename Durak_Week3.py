import tkinter as tk
from tkinter import messagebox

# Initialize an empty list to store tasks
tasks = []

# Initialize counters for indexing tasks and assigning Sequence Numbers
index_counter = 1
sqnumber_counter = 1

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            # Write each task to the file
            f.write(f"{task['Index Number']},{task['Sequence Number'] if 'Sequence Number' in task else ''},{task['Task Name']},{task['Status']}\n")
    # Show a success message
    messagebox.showinfo("Success", "Tasks saved successfully.")

# Function to load tasks from a file
def load_tasks():
    global index_counter, sqnumber_counter
    try:
        with open("tasks.txt", "r") as f:
            tasks.clear()
            for line in f:
                # Parse each line of the file and create tasks
                parts = line.strip().split(',')
                task = {
                    "Index Number": int(parts[0]),
                    "Sequence Number": int(parts[1]) if parts[1] else None,
                    "Task Name": parts[2],
                    "Status": parts[3]
                }
                tasks.append(task)
                # Update index_counter and sqnumber_counter
                index_counter = max(index_counter, task['Index Number'] + 1)
                if task["Sequence Number"]:
                    sqnumber_counter = max(sqnumber_counter, task["Sequence Number"] + 1)
        # Refresh the task list in the GUI
        refresh_task_list()
        # Show a success message
        messagebox.showinfo("Success", "Tasks loaded successfully.")
    except FileNotFoundError:
        # Show a message if no saved tasks found
        messagebox.showinfo("Info", "No saved tasks found.")

# Function to add a new task
def add_task():
    global index_counter, sqnumber_counter
    task_name = task_entry.get()
    if task_name:
        # Check existing Sequence Numbers and select an empty number
        used_sqnumbers = [task.get("Sequence Number", None) for task in tasks if task['Status'] != 'Deleted']
        if used_sqnumbers:
            sqnumber_counter = max(used_sqnumbers) + 1
        # Create a new task
        task = {
            "Index Number": index_counter,
            "Sequence Number": sqnumber_counter,
            "Task Name": task_name,
            "Status": "Pending"
        }
        # Append the task to the list
        tasks.append(task)
        # Update counters
        index_counter += 1
        sqnumber_counter += 1
        # Show a success message
        messagebox.showinfo("Success", "Task added successfully.")
        # Clear the task entry field
        task_entry.delete(0, tk.END)
        # Refresh the task list in the GUI
        refresh_task_list()
    else:
        # Show an error message if the task name is empty
        messagebox.showerror("Error", "Task name cannot be empty.")

# Function to mark a task as completed or pending
def complete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = tasks[selected_index[0]]
        # Toggle between "Completed" and "Pending" status
        if selected_task["Status"] == "Deleted":
            messagebox.showerror("Error", "Cannot complete a deleted task.")
        else:
            if selected_task["Status"] == "Completed":
                selected_task["Status"] = "Pending"
            else:
                selected_task["Status"] = "Completed"
            # Show a success message
            messagebox.showinfo("Success", "Task status updated.")
            # Refresh the task list in the GUI
            refresh_task_list()
    else:
        # Show an error message if no task selected
        messagebox.showerror("Error", "Please select a task.")

# Function to mark a task as deleted
def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = tasks[selected_index[0]]
        selected_task["Status"] = "Deleted"
        # Show a success message
        messagebox.showinfo("Success", "Task marked as deleted.")
        # Refresh the task list in the GUI
        refresh_task_list()
    else:
        # Show an error message if no task selected
        messagebox.showerror("Error", "Please select a task.")

# Function to display details of a task
def show_task_details():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = tasks[selected_index[0]]
        if selected_task['Status'] == 'Deleted':
            # Show only Index Number, Task Name, and Status for deleted tasks
            messagebox.showinfo("Task Details", f"Index Number: {selected_task['Index Number']}\nTask Name: {selected_task['Task Name']}\nStatus: {selected_task['Status']}")
        else:
            sqnumber_info = f"Sequence Number: {selected_task['Sequence Number']}" if 'Sequence Number' in selected_task else ""
            # Show Index Number, Sequence Number (if exists), Task Name, and Status for other tasks
            messagebox.showinfo("Task Details", f"Index Number: {selected_task['Index Number']}\n{sqnumber_info}\nTask Name: {selected_task['Task Name']}\nStatus: {selected_task['Status']}")
    else:
        # Show an error message if no task selected
        messagebox.showerror("Error", "Please select a task.")

# Function to display all tasks
def show_all_tasks():
    # Display all tasks with their Index Number, Sequence Number (if exists), Task Name, and Status
    all_tasks_text = "\n".join([f"Index: {task['Index Number']} | {'Sequence Number: ' + str(task['Sequence Number']) if 'Sequence Number' in task and task['Status'] != 'Deleted' else ''} | Task Name: {task['Task Name']} ({task['Status']})" for task in tasks])
    # Show all tasks in a messagebox
    messagebox.showinfo("All Tasks", all_tasks_text)

# Function to display completed tasks
def show_completed_tasks():
    # Filter out completed tasks
    completed_tasks = [task for task in tasks if task['Status'] == 'Completed']
    if completed_tasks:
        # Display completed tasks with their Index Number and Task Name
        completed_tasks_text = "\n".join([f"Index: {task['Index Number']} | Task Name: {task['Task Name']} ({task['Status']})" for task in completed_tasks])
        # Show completed tasks in a messagebox
        messagebox.showinfo("Completed Tasks", completed_tasks_text)
    else:
        # Show a message if no completed tasks found
        messagebox.showinfo("Completed Tasks", "No completed tasks found.")

# Function to display deleted tasks
def show_deleted_tasks():
    # Filter out deleted tasks
    deleted_tasks = [task for task in tasks if task['Status'] == 'Deleted']
    if deleted_tasks:
        # Display deleted tasks with their Index Number and Task Name
        deleted_tasks_text = "\n".join([f"Index: {task['Index Number']} | Task Name: {task['Task Name']} ({task['Status']})" for task in deleted_tasks])
        # Show deleted tasks in a messagebox
        messagebox.showinfo("Deleted Tasks", deleted_tasks_text)
    else:
        # Show a message if no deleted tasks found
        messagebox.showinfo("Deleted Tasks", "No deleted tasks found.")

# Function to refresh the task list displayed in the GUI
def refresh_task_list():
    # Clear the task listbox
    task_listbox.delete(0, tk.END)
    # Iterate over tasks and add them to the listbox
    for task in tasks:
        if task['Status'] == 'Deleted':
            # Display deleted tasks with their Index Number and Task Name
            task_listbox.insert(tk.END, f"Index: {task['Index Number']} | Task Name: {task['Task Name']} ({task['Status']})")
        else:
            sqnumber_info = f" | Sequence Number: {task['Sequence Number']}" if 'Sequence Number' in task else ""
            # Display other tasks with their Index Number, Sequence Number (if exists), Task Name, and Status
            task_listbox.insert(tk.END, f"Index: {task['Index Number']} {sqnumber_info} | Task Name: {task['Task Name']} ({task['Status']})")

# Function to exit the program
def exit_program():
    root.destroy()

# Create a tkinter window
root = tk.Tk()
root.title("Task Manager")

# Labels
title_label = tk.Label(root, text="Task Manager", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

task_label = tk.Label(root, text="Task Name:")
task_label.grid(row=1, column=0, sticky="w")

# Task Entry
task_entry = tk.Entry(root)
task_entry.grid(row=1, column=1, padx=5, pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=70)
task_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
refresh_task_list()

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

task_details_button = tk.Button(root, text="Task Details", command=show_task_details)
task_details_button.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

show_all_tasks_button = tk.Button(root, text="Show All Tasks", command=show_all_tasks)
show_all_tasks_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

show_completed_tasks_button = tk.Button(root, text="Show Completed Tasks", command=show_completed_tasks)
show_completed_tasks_button.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

show_deleted_tasks_button = tk.Button(root, text="Show Deleted Tasks", command=show_deleted_tasks)
show_deleted_tasks_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Save and load buttons
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

root.mainloop()

