"""Тесты повторяющихся задач."""

from src.services.recurrence import next_due_date


def test_daily_adds_one_day():
    """daily прибавляет ровно 1 день."""
    assert next_due_date("2026-11-10T15:00", "daily") == "2026-11-11T15:00:00"


def test_monthly_end_of_month():
    """monthly корректно переживает конец месяца."""
    result = next_due_date("2026-01-31T10:00", "monthly")
    assert result.startswith("2026-02-28")
