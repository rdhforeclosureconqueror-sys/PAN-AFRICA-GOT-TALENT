from app.workers.celery_app import celery_app


@celery_app.task(name="moderation.scan_entry")
def scan_entry(entry_id: str) -> dict:
    return {"entry_id": entry_id, "status": "clean"}
