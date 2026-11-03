"""Экспорт задач в формат iCalendar."""
from datetime import datetime

from icalendar import Calendar, Event

from src.models.task import Task


def export_ics(tasks: list[Task]) -> bytes:
    """Сгенерировать .ics по RFC 5545."""
    cal = Calendar()
    cal.add("prodid", "-//Task Planner//RU")
    cal.add("version", "2.0")
    for task in tasks:
        event = Event()
        event.add("summary", task.title)
        event.add("dtstart", datetime.fromisoformat(task.due_date))
        event.add("dtend", datetime.fromisoformat(task.due_date))
        event.add("uid", task.id)
        cal.add_component(event)
    return cal.to_ical()
