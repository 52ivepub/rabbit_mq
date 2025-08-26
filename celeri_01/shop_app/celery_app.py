from celery import Celery

app = Celery(
    "shop_app.celery_app",
    broker="amqp://user:password@localhost:5672//",
    backend="rpc://",
    include=["celeri_01.shop_app.tasks"]
)

