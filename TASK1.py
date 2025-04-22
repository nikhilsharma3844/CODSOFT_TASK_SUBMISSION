import json
import os

TODO_FILE = "todo_list.json"

# Load existing tasks from file or initialize an empty list
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")
    print()

# Add a new task
def add_task(tasks):
    title = input("Enter the task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added!\n")
    else:
        print("Task cannot be empty!\n")

# Mark a task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            print("Task marked as done!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(tasks):
            tasks.pop(idx - 1)
            print("Task deleted!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main app loop
def main():
    tasks = load_tasks()
    while True:
        print("To-Do List App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
