#!/usr/bin/env python

"""An exporter to fetch a fields value and count it for prometheus."""

from time import sleep

import prometheus_client as prom

from broker import KafkaHandler
from config import Config


service = Config().service
counter_name = Config().counter_name
header_fields = Config().header_fields
counter = prom.Counter(
    "{}_{}".format(service, counter_name),
    "The {}'s {} counter".format(service, (header_fields)),
    header_fields + ["service", "topic"]
)
exposed_port = Config().port


if __name__ == "__main__":
    prom.start_http_server(exposed_port)
    consumer = KafkaHandler()
    print("Daemon started successfully on port {} ...".format(exposed_port))
    for message in consumer.consume_loop():
        try:
            headers = {k: v.decode('utf-8')
                       for k, v in dict(message.headers()).items()}
            headers['service'] = service
            headers['topic'] = message.topic()
        except Exception as e:
            print("ERROR: ", e)
        finally:
            consumer.try_commit()
            try:
                counter.labels(**headers).inc()
            except Exception as e:
                print("ERROR: Error in mapping headers to configured ones", e)
                raise e
