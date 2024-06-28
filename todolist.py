import os

# Define the file where tasks will be stored
TASKS_FILE = "tasks.txt"

def load_tasks():
    
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    """Save tasks to the file"""
    with open(TASKS_FILE, "w") as file:
        file.write("\n".join(tasks))

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def show_tasks(tasks):
    """Display the list of tasks"""
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task(tasks):
    """Update an existing task"""
    show_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to update: ")) - 1
        tasks[task_index] = input("Enter the updated task: ")
        print(f"Task {task_index + 1} updated.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task from the list"""
    show_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        print(f"Task '{tasks.pop(task_index)}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
