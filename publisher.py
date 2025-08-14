import logging
from os import close
from httpx import get
import pika
from config import get_connection, configure_logging

log = logging.getLogger(__name__)


def produce_message(channel: pika.BlockingConnection):
    channel.basic_publish(
        excange="",
        rou
    )


def main():
    configure_logging()
    with get_connection() as connection:
        log.info("Created connection: %s", connection) 
        with connection.channel() as channel:
            log.info("Created channel: %s", channel) 
        
            while True:
                pass
         


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Bye!")

 