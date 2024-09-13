from celery import Celery

app = Celery("tasks", broker="redis://redis:6379/0")
app.conf.update(
    result_backend="redis://redis:6379/0",
)
