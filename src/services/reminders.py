"""Расчёт времени напоминания."""
from datetime import datetime, timedelta
from typing import Optional

from src.models.task import Task


def compute_remind_at(task: Task) -> Optional[str]:
    """Время напоминания = due_date - offset_minutes."""
    if task.reminder_offset_minutes is None:
        return None
    due = datetime.fromisoformat(task.due_date)
    return (due - timedelta(minutes=task.reminder_offset_minutes)).isoformat()
