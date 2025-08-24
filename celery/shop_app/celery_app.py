from celery import Celery

app = Celery(
    "shop_app.celery_app",
    broker="amqp://user:password@localhost:5672//",
    backend="rpc://",
)

