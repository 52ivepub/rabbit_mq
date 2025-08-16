import logging
from os import close
from re import L
import time
from typing import TYPE_CHECKING
from httpx import get
import pika
from config import get_connection, configure_logging

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel

log = logging.getLogger(__name__)


def produce_message(channel: "BlockingChannel"):
    queue = channel.queue_declare(queue='hello')
    log.info("Declared queue  %s %s", 'hello', queue)
    message_body = f"Hello world... from {time.time()}"
    log.info("Publish message %s", message_body)
    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body=message_body,
    )
    log.warning("Published message %s", message_body)


def main():
    configure_logging(level=logging.WARNING)
    with get_connection() as connection:
        log.info("Created connection: %s", connection) 
        with connection.channel() as channel:
            log.info("Created channel: %s", channel) 
            produce_message(channel=channel)
        
            # while True:
            #     pass
         


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Bye!")

 