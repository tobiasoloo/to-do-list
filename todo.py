import openai

class Task:
    def __init__(self, task_id: int, description: str, done: bool = False):
        self.task_id = task_id
        self.description = description
        self.done = done

    def __str__(self):
        status = "✅" if self.done else "❌"
        return f"{self.task_id}. {self.description} [{status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description: str):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        print(f"Task {task.task_id} added: {description}")
        self.next_id += 1

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in to-do list.")
        else:
            for task in self.tasks:
                print(task)

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.task_id == task_id:
                task.done = True
                print(f"Task {task_id} marked done.")
                return
        print(f"No task with id {task_id}")

    def suggest_task(self):
        open_tasks = [t for t in self.tasks if not t.done]
        if not open_tasks:
            print("No open tasks to suggest on.")
            return

        # Build prompt
        task_list = "\n".join([f"{t.task_id}. {t.description}" for t in open_tasks])
        prompt = f"I have these tasks:\n{task_list}\nWhich one should I do next and why?"

        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  # fast + inexpensive model
                messages=[{"role": "user", "content": prompt}],
            )
            suggestion = response.choices[0].message.content
            print("Suggestion from AI:")
            print(suggestion)
        except Exception as e:
            print("AI suggestion failed:", e)


def main():
    todo = ToDoList()

    while True:
        print("\nOptions: [1] Add [2] List [3] Complete [4] Suggest [0] Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            desc = input("Enter task description: ").strip()
            todo.add_task(desc)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            try:
                tid = int(input("Enter task id to complete: "))
                todo.complete_task(tid)
            except ValueError:
                print("Invalid id.")
        elif choice == "4":
            todo.suggest_task()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
