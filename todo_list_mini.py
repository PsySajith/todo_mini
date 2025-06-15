tasks = []

def show_menu():
    print("\n====== Task Mate ======")
    print("1. Add Task\n2. View Task\n3. Complete Task\n4. Delete Task\n5. Exit")

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({"name": task_name,"completed" : False})
    print(f"task {task_name} added")

def view_task():
    if not tasks:
        print("No tasks")
        return

    for t in range(len(tasks)):
        print(f"{t + 1}. {tasks[t]['name']} [{'✔' if tasks[t]['completed'] else '✘'}]")


def update_task():
    view_task()
    try:
        task = int(input("Enter task number: ")) - 1
        tasks[task]['completed'] = True
        print("task completed")
    except (ValueError,IndexError):
        print("Invalid number.")

def delete_task():
    view_task()
    try:
        tasks.pop(int(input("Enter task number: ")) -1)
        print("task deleted")
    except (ValueError,IndexError):
        print(f"Invalid number")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("invalid choice")