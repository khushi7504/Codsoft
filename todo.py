# Simple To-Do List Application

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(task_list):
    task = input("Enter the task description: ")
    task_list.append(task)
    print("Task added.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(task_list):
                removed_task = task_list.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            delete_task(task_list)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if _name_ == "_main_":
    main()
