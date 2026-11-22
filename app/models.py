class Task:
    def __init__(self, task_id: int, title: str, status: str = "pending"):
        self.id = task_id
        self.title = title
        self.status = status