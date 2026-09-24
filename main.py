tasks = []

def add_task():
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- TASKS ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            raise ValueError

        deleted = tasks.pop(number - 1)
        print(f"Task deleted: {deleted}")

    except ValueError:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()