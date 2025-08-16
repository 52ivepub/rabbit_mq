import pika
import logging

RMQ_HOST = '0.0.0.0'
RMQ_PORT = 5672

# RMQ_USER = 'user'
# RMQ_PASSWORD = 'password'
MQ_EXCHANGE=""
MQ_ROUTING_KEY="newwwwwwq"

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=pika.PlainCredentials(username="user", password="password")
)

def get_connection():
    return pika.BlockingConnection(
        parameters=connection_params,
    )


def configure_logging(level: int = logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(funcName)20s %(module)s:%(lineno)d %(levelname)-8s - %(message)s"
    )