from fastapi import FastAPI
from app.tasks import long_task

app = FastAPI()


@app.post("/tasks")
def create_task(seconds: int = 10):
    task = long_task.delay(seconds)
    return {
        "task_id": task.id,
        "status": "queued",
    }


@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    from app.celery_app import celery_app

    result = celery_app.AsyncResult(task_id)

    response = {
        "task_id": task_id,
        "state": result.state,
    }

    if result.state == "PROGRESS":
        response["progress"] = result.info

    if result.state == "SUCCESS":
        response["result"] = result.result

    if result.state == "FAILURE":
        response["error"] = str(result.info)

    return response
