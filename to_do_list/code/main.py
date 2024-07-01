# --------------- Section : Imports --------------- #
from task_operations import *
from Utilities import clear_screen, header_msg, get_choice

# --------------- Section : Main Function --------------- #
if __name__ == "__main__":
    while True :
        clear_screen()
        header_msg()
        view_tasks()
        choice = get_choice()
        match choice :                
            case 1 :
                new_task = create_task()
                add_task(new_task)
                print('Task is added successfully')
                input('Press enter ')
            case 2 :
                task_number = get_task_number()
                removed_task = get_task(task_number)
                if removed_task == {} :
                    pass
                else:
                    is_removed = remove_task(removed_task)
                    if is_removed:
                        print('Task is removed successfully')
                    else :
                        pass
                    input('Press enter ')
            case 3 :
                complete_task()
                input('Press enter ')
            case 4 :
                due_date()
                input('Press enter ')
            case 5:
                task_number = get_task_number()
                view_details(task_number - 1)
                input('Press enter ')
            case 6 :
                sort_priority_level()    
                input('Press enter ')
        