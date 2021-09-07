#!/usr/bin/env python

"""An exporter to fetch a fields value and count it for prometheus."""

import prometheus_client as prom

from broker import KafkaHandler
from config import Config


header_field = Config().header_field
service = Config().service
counter_name = Config().counter_name
counter = prom.Counter(
    counter_name,
    "The {}'s {} counter".format(service, header_field),
    [header_field]
)
exposed_port = Config().port


def export_header_field_value(headers, header_field=header_field):
    value = None
    while value is None:
        item = headers.pop()
        if item[0] == header_field:
            value = item[1]
    return value


if __name__ == "__main__":
    prom.start_http_server(exposed_port)
    consumer = KafkaHandler()
    for message in consumer.consume_loop():
        try:
            headers = message.headers()
            api_index_id = export_header_field_value(headers, header_field)
            consumer.try_commit()
            counter.labels(int(api_index_id)).inc()
        except Exception as e:
            print("Unhandled error ", e)
