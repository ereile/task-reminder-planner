from src.models.task import Task, TaskStatus


class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, title: str, due_date, description: str = "", priority=None) -> Task:
        task = Task(title=title, due_date=due_date, description=description,
                    priority=priority or Task.priority)
        self.repository.save(task)
        return task

    def mark_done(self, task_id: str) -> None:
        raise NotImplementedError("mark_done is not implemented yet")
