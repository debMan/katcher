from confluent_kafka import Consumer
from confluent_kafka.cimpl import KafkaError, KafkaException

from config import Config


kafka = Config()
topics = kafka.topics
address = ",".join(kafka.address)


class KafkaHandler:
    def __init__(
            self,
            address=address,
            group_id=kafka.consumer,
            topics=topics):
        connection = {'bootstrap.servers': address,
                      'group.id': group_id,
                      'auto.offset.reset': kafka.offset_reset,
                      'session.timeout.ms': kafka.timeout,
                      'enable.auto.commit': False}
        self.consumer = Consumer(connection)
        self.msg_count = 0
        self.MIN_COMMIT_COUNT = 1
        self.consumer.subscribe(topics)

    def consume_loop(self):
        try:
            running = True
            while running:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        print('%% %s [%d] reached end at offset %d\n' %
                              (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    yield msg
        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()

    def try_commit(self):
        self.msg_count += 1
        if self.msg_count % self.MIN_COMMIT_COUNT == 0:
            self.consumer.commit(asynchronous=False)
            self.msg_count = 0
