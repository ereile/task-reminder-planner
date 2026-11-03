"""Точка входа FastAPI."""

import json
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

from src.models.task import Task
from src.services.ical import export_ics
from src.services.recurrence import next_due_date
from src.services.reminders import compute_remind_at

DATA = Path("data/tasks.json")
DATA.parent.mkdir(exist_ok=True)
if not DATA.exists():
    DATA.write_text("[]", encoding="utf-8")

app = FastAPI(title="Task & Reminder Planner", version="0.1.0")


def load_tasks() -> list[Task]:
    """Загрузить задачи из JSON."""
    return [Task(**item) for item in json.loads(DATA.read_text(encoding="utf-8"))]


def save_tasks(tasks: list[Task]) -> None:
    """Сохранить задачи в JSON."""
    DATA.write_text(
        json.dumps([t.to_dict() for t in tasks], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


@app.post("/tasks")
def create_task(task: Task) -> dict:
    """Создать задачу, вернуть id и время напоминания."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return {"id": task.id, "remind_at": compute_remind_at(task)}


@app.get("/tasks")
def list_tasks(status: str | None = None, priority: str | None = None) -> list[Task]:
    """Список задач с фильтрацией."""
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t.status == status]
    if priority:
        tasks = [t for t in tasks if t.priority == priority]
    return tasks


@app.patch("/tasks/{task_id}/done")
def mark_done(task_id: str) -> dict:
    """Отметить выполненной; для повторяющейся — создать следующую."""
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.status = "done"
            nxt = next_due_date(task.due_date, task.recurrence)
            if nxt:
                clone = Task(
                    **{
                        **task.to_dict(),
                        "id": str(uuid4()),
                        "due_date": nxt,
                        "status": "active",
                    }
                )
                tasks.append(clone)
            save_tasks(tasks)
            return {"ok": True, "next": nxt}
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/tasks/export.ics")
def export_calendar() -> Response:
    """Экспорт всех задач в iCal."""
    ics = export_ics(load_tasks())
    return Response(content=ics, media_type="text/calendar")
