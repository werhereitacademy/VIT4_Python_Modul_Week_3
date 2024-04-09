#<<<<<<< HEAD

print("""Project Description: In this assignment, you will create a task manager 
application using the Python programming language. This application 
will allow users to add, complete, delete, and list their tasks.""")





task=[]

def add_task ():
    return

def completed_task ():
    return

def del_task ():
 
    return

def list_completed_task():
    return

def statusList_task ():
    return

while True :
    print("""
|===========Task Manager Application======[-][o][x]
|          T A S K   M  E  N  U                   | 
|   1- Add Task                                   | 
|   2- completed Task                             | 
|   3- Delete Task                                |
|   4- List Completed Task                        | 
|   5- List Satatus                               | 
|   6- Exit                                       | 
|               version 3.02                      |       
|           copyright@vit4 group2                 |
|=================================================| """)

    choise_task= input("Please Enter the a nummer:")

    if choise_task == "1":
        add_task()

    elif choise_task == "2":
        comp_task()

    elif choise_task == "3":
        del_task()
    elif choise_task == "4":
        list_completed_task()

    elif statusList_task == "5":
        comp_task()
    
    elif choise_task == "6":
         break
    else:
        print("Invalid option! Please try again.")
       

        



    

