import json

class Task:
    def __init__(self, description, due_date=None, priority=0, completed=False, details=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.details = details

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, priority=0, details=None):
        task = Task(description, due_date, priority, False, details)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task.description} - {'Completed' if task.completed else 'Pending'}")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def set_due_date(self, task_index, due_date):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].due_date = due_date

    def set_priority(self, task_index, priority):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].priority = priority

    def sort_by_priority(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

    def add_details(self, task_index, details):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].details = details

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.tasks = [Task(**task) for task in data]
from todo_list import ToDoList

def print_menu():
    print("==== To-Do List Menu ====")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Exit")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = int(input("Enter priority level (0 for lowest): "))
            details = input("Enter additional details (optional): ")
            todo_list.add_task(description, due_date, priority, details)
            print("Task added successfully!")

        elif choice == '2':
            todo_list.view_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
            print("Task marked as completed!")

        elif choice == '3':
            print("=== Tasks ===")
            todo_list.view_tasks()

        elif choice == '4':
            todo_list.view_tasks()
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(task_index)
            print("Task deleted successfully!")

        elif choice == '5':
            filename = input("Enter file name to save tasks: ")
            todo_list.save_to_file(filename)
            print("Tasks saved to file successfully!")

        elif choice == '6':
            filename = input("Enter file name to load tasks: ")
            todo_list.load_from_file(filename)
            print("Tasks loaded from file successfully!")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
