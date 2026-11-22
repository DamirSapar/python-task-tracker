from app.models import Task


class PriorityStrategy:
    def get_weight(self) -> int:
        raise NotImplementedError


class HighPriorityStrategy(PriorityStrategy):
    def get_weight(self) -> int:
        return 1


class DefaultPriorityStrategy(PriorityStrategy):
    def get_weight(self) -> int:
        return 3


class TaskService:
    def __init__(self):
        self.tasks = []
        self._strategies = {
            "high": HighPriorityStrategy(),
            "medium": DefaultPriorityStrategy(),
            "low": DefaultPriorityStrategy(),
        }

    def create_task(self, title: str, priority: str = "medium"):
        # Fix for Risk R-01: Validation for empty or whitespace-only title
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = Task(len(self.tasks) + 1, title.strip())
        task.priority = priority
        strategy = self._strategies.get(priority, DefaultPriorityStrategy())
        task.weight = strategy.get_weight()
        self.tasks.append(task)
        return task

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "completed"
                return task
        return None