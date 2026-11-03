"""Модель задачи."""

from dataclasses import asdict, dataclass, field
from typing import Optional
from uuid import uuid4


@dataclass
class Task:
    """Задача планировщика."""

    title: str
    due_date: str
    id: str = field(default_factory=lambda: str(uuid4()))
    description: str = ""
    priority: str = "medium"
    status: str = "active"
    recurrence: str = "none"
    reminder_offset_minutes: Optional[int] = None

    def to_dict(self) -> dict:
        """Сериализация в словарь."""
        return asdict(self)
