"""Логика повторяющихся задач."""
from datetime import datetime, timedelta
from typing import Optional

from dateutil.relativedelta import relativedelta


def next_due_date(due_date: str, recurrence: str) -> Optional[str]:
    """Следующая дата: +1 день / +7 дней / +1 месяц."""
    if recurrence == "none":
        return None
    due = datetime.fromisoformat(due_date)
    if recurrence == "daily":
        nxt = due + timedelta(days=1)
    elif recurrence == "weekly":
        nxt = due + timedelta(weeks=1)
    elif recurrence == "monthly":
        nxt = due + relativedelta(months=1)
    else:
        return None
    return nxt.isoformat()
