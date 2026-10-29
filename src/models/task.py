from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskStatus(str, Enum):
    ACTIVE = "active"
    DONE = "done"
    OVERDUE = "overdue"


@dataclass
class Task:
    title: str
    due_date: datetime
    description: str = ""
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = TaskStatus.ACTIVE
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Task title must not be empty")
        if self.due_date is None:
            raise ValueError("Task due_date is required")
