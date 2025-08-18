import logging
import time
from typing import TYPE_CHECKING
from config import (
    MQ_ROUTING_KEY,
    get_connection,
    configure_logging,
    )

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel

log = logging.getLogger(__name__)


def declare_queue(channel: "BlockingChannel"):
    queue = channel.queue_declare(queue=MQ_ROUTING_KEY)
    log.info("Declared queue  %s %s", MQ_ROUTING_KEY, queue)

    

def produce_message(channel: "BlockingChannel", idx: int):
    message_body = f"New message # {idx:02d}"
    log.info("Publish message %s", message_body)
    channel.basic_publish(
        exchange="",
        routing_key=MQ_ROUTING_KEY,
        body=message_body,
    )
    log.warning("Published message %s", message_body)


def main():
    configure_logging(level=logging.WARNING)
    with get_connection() as connection:
        log.info("Created connection: %s", connection) 
        with connection.channel() as channel:
            log.info("Created channel: %s", channel)
            declare_queue(channel=channel)
            for idx in range(1, 11):          
                produce_message(channel=channel, idx=idx)   
                time.sleep(2)
                 
        
            # while True:
            #     pass
         


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Bye!")

 