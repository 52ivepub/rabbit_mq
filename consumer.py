import logging
import time
from typing import TYPE_CHECKING
import pika
from config import MQ_ROUTING_KEY, get_connection, configure_logging
from rabbit import RabbitBase

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
    log.warning("[ ] Start processing message %r", body)

    start_time = time.time()
    number = int(body[-2:])
    is_odd = number % 2
    time.sleep(1 + is_odd * 2)
    end_time = time.time()
    # log.info("[X] Finished processing message %r sending ack", body)    
    ch.basic_ack(delivery_tag=method.delivery_tag)
    log.warning(
        "[X] Finished in %.2fs processing message %r",
        end_time-start_time,
        body,
        )    
    

def consume_messages(channel: "BlockingChannel"):
    channel.basic_qos(prefetch_count=1)
    channel.queue_declare(MQ_ROUTING_KEY)
    channel.basic_consume(
        queue=MQ_ROUTING_KEY,
        on_message_callback=process_new_message,
        # auto_ack=True,
    )
    log.warning("Waiting for message")
    channel.start_consuming()


def main():
    configure_logging(level=logging.WARNING)
    with RabbitBase() as robbit:
        consume_messages(channel=robbit.channel)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Bye!")

 