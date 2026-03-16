tasks = {}


def add_task():
    task = input("Enter a task: ").capitalize()
    time = input("Enter time (Morning/Afternoon/Evening): ").capitalize()

    if task in tasks:
        tasks[task] += " & " + time
    else:
        tasks[task] = time
    return "Task added ✔️"


def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return

    else:
        print(f"{"Number":<8} | {"Tasks":<8} | {"Time"}")
        print("==================================")

        for i, task in enumerate(tasks, start=1):
            print(f"{i:<8} | {task:<8} | {tasks[task]}")
        print("----------------------------------")


def remove_task():
    view_tasks()

    try:
        num = int(input("\nEnter the task number to remove: "))

        task_name = list(tasks.keys())[num - 1]
        tasks.pop(task_name)

        return f"Task: ({task_name})removed.❌"

    except:
        return "Please enter a valid number."


print("""
1 Add task
2 View taskes
3 Remove task
4 Exit
    """)

while True:
    choice = input("\nChoose an option: ")

    if choice == "1":
        print(add_task())

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        print(remove_task())

    elif choice == "4":
        print("Have a nice rest of your day!")
        break

    else:
        print("Choose between 1-4.")
