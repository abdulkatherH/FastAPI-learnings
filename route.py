from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
tasks = []
class Task(BaseModel):
    id: int
    title: str
    description: str

@router.get('/tasks')
def get_tasks():
    if not tasks:
        raise HTTPException(status_code='404', detail= 'YOUR TASK WERE NOT FOUND')
    return tasks

@router.get('/tasks/{task_id}')
def get_task_by_id(task_id: int):
    for task in tasks:
        if task_id == task_id:
            return task
    
    raise HTTPException(status_code='404', detail='The task you entered is not found')

@router.post('/tasks')
def create_task(task: Task):
    tasks.append(task)
    return task

@router.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task_id == task_id:
            tasks.pop(index)

            return {'Message': 'Task deleted successfully'}
    raise HTTPException(status_code=404, detail='The task you entered is not found!')

