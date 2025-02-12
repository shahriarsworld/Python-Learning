def todo_list():
    tasks = []

    print("To-Do List Application")
    print("Enter 'add' to add a task, 'remove' to remove a task, 'view' to see all tasks, and 'q' to quit.")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == 'add':
            task = input("Enter task: ").strip()
            tasks.append(task)
            print(f"Added task: {task}")
        elif command == 'remove':
            task = input("Enter task to remove: ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Removed task: {task}")
            else:
                print(f"Task not found: {task}")
        elif command == 'view':
            print("To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif command == 'q':
            break
        else:
            print("Invalid command. Please try again.")

todo_list()
