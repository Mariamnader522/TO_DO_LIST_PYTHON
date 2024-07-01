from datetime import datetime
import json, os

# ========================================================================= #
def get_task_name() -> str :
    """
        A function gets the task name from the user
    """
    return input("Enter the task name: ")

# ========================================================================= #

def get_task_due_date() :
    """
        A function gets the task due date from user.
    """
    while True:
        date = input ("date is(yyyy-mm-dd,hh:mm:ss):")
        if date.isalpha :
            date_form = datetime.strptime(date,'%Y-%m-%d,%H:%M:%S')
            return date_form
        else:
            print("please, try again!")
            continue

# ========================================================================= #

def get_task_priority() -> bool:
    """
        A function gets the task details from user.
    """
    while True :                                    # Ask the user if he want to give this task priority
        print("Do you want to prioritize this task ?")
        temp_choice = input("y or n ?")
        if ('y' == temp_choice) or ('n' == temp_choice) or ('Y' == temp_choice) or ('N' == temp_choice):
            break
        else :
            print('Invalid Input, Please Try again')
            continue

    match temp_choice :
        case 'y' :
            return True
        case 'Y' :
            return True
        case 'n' :
            return False
        case 'N' :
            return False
        case _:
            return False

# ========================================================================= #

def get_task_number() :
    """
        A function gets the task number from user.
    """
    while True :
        try :
            task_number = int(input('Enter the task number: '))
            return task_number
        except :
            print("Invalid Input, Please try again ")
            continue

# ========================================================================= #

def get_task(task_number) -> dict:
    """
        A function gets the task due date from user.
        @param task_number : The number of the task.
        @returns : The dictionary of the task needed.
    """
    try:
        with open("Tasks.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Tasks file not found")
        return {}
    
    if 0 == len(data["Tasks"]) :
        print("No tasks exist")
        return {} 
    else :
        pass

    if task_number > 0 and task_number <= len(data["Tasks"]):
        return data["Tasks"][task_number-1]
    else:
        return {}

# ========================================================================= #

def clear_screen():
    """
        A function clears the terminal
    """
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# ========================================================================= #

def header_msg() :
    print("|------------------------------------------------|")
    print("|------------ To-do-list Application ------------|")
    print("|------------------------------------------------|")

# ========================================================================= #

def choices_msg() :
    print('Chose what you want to do :')
    print('1- New Task.\t\t\t\t2- Remove Task.')
    print('3- Complete Task\t\t\t4- Due-date of a task')
    print('5- View details of a task.\t\t6- Tasks By Priority.')

# ========================================================================= #

def get_choice() -> int:
    while True :
        try :
            choices_msg()
            choice = int(input())
            if (0 < choice ) and (7 >= choice) :
                return choice
            else :
                print('Invalid Input, Please try again')
        except :
            clear_screen()
            print('Invalid Input, Please try again')
            