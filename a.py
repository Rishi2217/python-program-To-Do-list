
def display_todo_list():
    print("\n--- To-Do List ---")
    if not tasks:
        print("No tasks at the moment.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")


def remove_task():
    display_todo_list()
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


tasks = []

while True:
    print("\n--- To-Do List Application ---")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_todo_list()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
