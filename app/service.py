from app.models import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def create_task(self, title: str):
        task = Task(len(self.tasks) + 1, title)
        self.tasks.append(task)
        return task

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "completed"
                return task
        return None