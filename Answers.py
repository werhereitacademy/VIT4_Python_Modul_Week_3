
print("""Project Description: In this assignment, you will create a task manager 
application using the Python programming language. This application 
will allow users to add, complete, delete, and list their tasks.""")





tasks=[]

def add_task(task_name, status="Pending"):
    if status not in ["Pending", "Completed"]:
        print("Invalid status!")
        return
    task = {
        "Sequence Number": len(tasks) + 1,
        "Task Name": task_name,
        "Status": status
    }
    tasks.append(task)
    print("New task added:", task_name, "- Status:", status)

def completed_task ():
    return

def del_task ():
 
    return

def list_completed_tasks():
    completed_tasks = [task for task in tasks if task["Status"] == "Completed"]
    if completed_tasks:
        print("Completed Tasks:")
        for index, task in enumerate(completed_tasks, start=1):
            print(f"{index}. {task['Task Name']}")
    else:
        print("No tasks have been completed yet.")



def list_all_tasks():
    if tasks:
        print("All Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['Task Name']} - Status: {task['Status']}")
    else:
        print("No tasks have been added yet.")


while True :
    print("""
|===========Task Manager Application======[-][o][x]
|          T A S K   M  E  N  U                   | 
|   1- Add Task                                   | 
|   2- completed Task                             | 
|   3- Delete Task                                |
|   4- List Comleted Tasks                        | 
|   5- List All Tasks                             | 
|   6- Exit                                       | 
|               version 3.02                      |       
|           copyright@vit4 group2                 |
|=================================================| """)

    choise_task= input("Please Enter the a nummer:")

    if choise_task == "1":
        task_name = input("Enter the name of the new task: ")
        status_input = input("Enter the status of the task 'Completed' or 'Pending' (default is 'Pending'): ").capitalize()
        if status_input:
            add_task(task_name, status_input)
        else:
            add_task(task_name)

    elif choise_task == "2":
        task_number = int(input("Enter the number of the completed task: "))
        complete_task(task_number)

    elif choise_task == "3":
        del_task()
    elif choise_task == "4":
        list_completed_tasks()

    elif choise_task == "5":
        list_all_tasks()

    elif choise_task == "6":

        print("Exiting the program...")
        break

    else:
        print("Invalid option! Please try again.")
       

        



    

