class ReminderService:
    def __init__(self, repository):
        self.repository = repository

    def create_reminder(self, task_id: str, remind_at):
        raise NotImplementedError("create_reminder stub")
