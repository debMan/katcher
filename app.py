import prometheus_client as prom

from broker import KafkaHandler
from config import Config

header_field = Config().header_field
service = Config().service
counter_name = Config().counter_name

def export_header_field_value(headers, header_field=header_field):
    value = None
    while value is None:
        item = headers.pop()
        if item[0] == header_field:
            value = item[1]
    return value


if __name__ == "__main__":
    counter = prom.Counter(
        counter_name,
        "The {}'s {} counter".format(service, header_field),
        [header_field, 'id']
    )
    prom.start_http_server(8080)
    consumer = KafkaHandler()
    for message in consumer.consume_loop():
        api_index_id = None
        try:
            headers = message.headers()
            id = export_header_field_value(headers, header_field)
            counter.label(header_field, id).inc()
            consumer.try_commit()
        except Exception as e:
            print("Unhandled error ", e)