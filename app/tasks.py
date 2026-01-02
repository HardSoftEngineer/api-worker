import time
from app.celery_app import celery_app


@celery_app.task(bind=True)
def long_task(self, seconds: int):
    for i in range(seconds):
        time.sleep(1)
        self.update_state(
            state="PROGRESS",
            meta={"current": i + 1, "total": seconds},
        )
    return {"status": "done", "duration": seconds}
