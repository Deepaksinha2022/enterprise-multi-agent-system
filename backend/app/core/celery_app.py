from celery import Celery

celery_app = Celery(
    "multi_agent_system",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

# broker holds tasks until a worker picks them up
# backend - stores output of completed tasks

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_routes={
        "app.core.tasks.run_research": {
            "queue": "research"
        },
        "app.core.tasks.add": {
            "queue": "default"
        },
    },
)
