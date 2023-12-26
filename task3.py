class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task.description}" added successfully!')

    def display_tasks(self):
        print("\nTask List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.description} - Due: {task.due_date}, Priority: {task.priority}, Completed: {task.completed}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print(f'Task "{task.description}" marked as completed!')
        else:
            print("Invalid task index.")

    def update_task(self, task_index, description=None, due_date=None, priority=None):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = description if description else task.description
            task.due_date = due_date if due_date else task.due_date
            task.priority = priority if priority else task.priority
            print(f'Task updated successfully: "{task.description}"')
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task.description}" removed successfully!')
        else:
            print("Invalid task index.")

# Example usage:
todo_list = ToDoList()

task1 = Task("Complete Python project", "2023-01-31", "High")
task2 = Task("Read a book", "2023-02-15", "Medium")
task3 = Task("Exercise", "2023-02-28", "Low")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

todo_list.display_tasks()

todo_list.mark_completed(1)
todo_list.display_tasks()

todo_list.update_task(2, description="Read two books")
todo_list.display_tasks()

todo_list.remove_task(3)
todo_list.display_tasks()
