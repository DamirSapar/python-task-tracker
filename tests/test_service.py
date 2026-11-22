from app.service import TaskService

def test_create_task():
    service = TaskService()
    task = service.create_task("Write report")
    assert task.id == 1
    assert task.title == "Write report"
    assert task.status == "pending"

def test_complete_task():
    service = TaskService()
    task = service.create_task("Write report")
    completed_task = service.complete_task(task.id)
    assert completed_task.status == "completed"