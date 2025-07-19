# to_do_list_cli.py

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(todo_list, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title, "completed": False})
    print("Task added successfully.")

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter task number to mark completed: ")) - 1
        todo_list[index]["completed"] = True
        print("Task marked as completed.")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        deleted = todo_list.pop(index)
        print(f"Deleted task: {deleted['title']}")
    except:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List.")
        break
    else:
        print("Invalid choice. Try again.")