"""Тесты экспорта в iCal."""
from src.models.task import Task
from src.services.ical import export_ics


def test_export_contains_vevent():
    """Файл .ics содержит VEVENT и SUMMARY."""
    task = Task(title="Demo", due_date="2026-11-10T15:00")
    ics = export_ics([task]).decode()
    assert "BEGIN:VEVENT" in ics
    assert "SUMMARY:Demo" in ics
