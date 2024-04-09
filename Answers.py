print("""Project Description: In this assignment, you will create a task manager 
application using the Python programming language. This application 
will allow users to add, complete, delete, and list their tasks.""")





task=[]

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

def comp_task ():
    return

def del_task ():
    return

def statusList_task ():
    return

while True :
    print("""
|===========Task Manager Application======[-][o][x]
|          T A S K   M  E  N  U                   | 
|   1- Add a Task                                 | 
|   2- Mark a Task as Completed                   | 
|   3- Delete a Task                              |
|   4- List Completed Tasks                       | 
|   5- List All Tasks With Status                 | 
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
        comp_task()

    elif choise_task == "3":
        del_task()

    elif statusList_task == "4":
        comp_task()
    
    elif choise_task == "5":
         break
    else:
        print("Invalid option! Please try again.")
       

        



    