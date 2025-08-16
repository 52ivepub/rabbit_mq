import logging
import time
from typing import TYPE_CHECKING
from httpx import get
import pika
from config import get_connection, configure_logging

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel
    from pika.spec import Basic, BasicProperties

log = logging.getLogger(__name__)


def process_new_message(
        ch: "BlockingChannel",
        method: "Basic.Deliver",
        properties: "BasicProperties",
        body: bytes,
):
    log.debug("ch: %s", ch) 
    log.debug("method: %s", method) 
    log.debug("properties: %s", properties) 
    log.debug("body: %s", body) 
    log.info("[ ] Start processing message %r", body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    log.warning("[X] Finished processing message %r ", body)    

def consume_messages(channel: "BlockingChannel"):
    channel.basic_consume(
        queue="hello",
        on_message_callback=process_new_message,
        # auto_ack=True,
    )
    log.warning("Waiting for message")
    channel.start_consuming()


def main():
    configure_logging(level=logging.INFO)
    with get_connection() as connection:
        log.info("Created connection: %s", connection) 
        with connection.channel() as channel:
            log.info("Created channel: %s", channel) 
            consume_messages(channel=channel)
        
            # while True:
            #     pass
         


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Bye!")

 