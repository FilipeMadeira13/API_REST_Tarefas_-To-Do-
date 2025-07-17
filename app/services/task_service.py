from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.domain.models import Task
from app.domain.schemas import TaskCreate, TaskUpdate


def create_task(session: Session, task: TaskCreate):
    db_task = Task(**task.model_dump())
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


def get_tasks(session: Session):
    tasks = session.exec(select(Task)).all()
    return tasks


def get_task(session: Session, task_id: int):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada"
        )
    return task


def update_task(session: Session, updated_task: TaskUpdate, task_id: int):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada"
        )

    task_data = updated_task.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def delete_task(session: Session, task_id: int):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada"
        )
    session.delete(task)
    session.commit()
