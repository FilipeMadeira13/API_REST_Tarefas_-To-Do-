from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.domain.schemas import TaskCreate, TaskRead, TaskUpdate
from app.infra.database import engine, get_session
from app.services.task_service import (
    create_task,
    delete_task,
    get_task,
    get_tasks,
    update_task,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create(task: TaskCreate, session: Session = Depends(get_session)):
    return create_task(session, task)


@router.get("/", response_model=list[TaskRead])
def get_all(session: Session = Depends(get_session)):
    return get_tasks(session)


@router.get("/{task_id}", response_model=TaskRead)
def get(task_id: int, session: Session = Depends(get_session)):
    return get_task(session, task_id)


@router.put("/{task_id}", response_model=TaskRead)
def update(
    updated_task: TaskUpdate, task_id: int, session: Session = Depends(get_session)
):
    return update_task(session, updated_task, task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(task_id: int, session: Session = Depends(get_session)):
    return delete_task(session, task_id)
