import os

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, task_desc):
        # Automatically adds the empty checkbox [ ]
        task = f"[ ] {task_desc}"
        self.tasks.append(task)
        self.save_tasks()
        print("Task added.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            if "[x]" in self.tasks[index]:
                print("Task is already completed.")
            else:
                # Slice the string to remove "[ ] " and replace with "[x] "
                # We assume the first 4 characters are "[ ] "
                task_desc = self.tasks[index][4:]
                self.tasks[index] = f"[x] {task_desc}"
                self.save_tasks()
                print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Mark Completed\n5. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.show_tasks()
            
            elif choice == "2":
                task = input("Enter the task: ")
                self.add_task(task)
            
            elif choice == "3":
                self.show_tasks()
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    self.delete_task(index)
                except ValueError:
                    print("Invalid input.")
            
            elif choice == "4":
                self.show_tasks()
                try:
                    index = int(input("Enter task number to mark completed: ")) - 1
                    self.mark_completed(index)
                except ValueError:
                    print("Invalid input.")
            
            elif choice == "5":
                print("Exiting task manager.")
                break
            
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    manager = TaskManager()
    manager.run()