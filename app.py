#!/usr/bin/env python

"""An exporter to fetch a fields value and count it for prometheus."""

from time import sleep

import prometheus_client as prom
import sentry_sdk

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
sentry = Config().sentry

if sentry is not None:
    sentry_sdk.init(
        dsn = sentry.get("dsn"),
        release = sentry.get("release"),
        environment = sentry.get("environment"),
        send_default_pii = sentry.get("send-default-pii"),
        debug = sentry.get("debug"),
        traces_sample_rate = sentry.get("traces-sample-rate")
    )

welcome_message = \
    "Daemon started successfully on port {} ...".format(exposed_port)


if __name__ == "__main__":
    prom.start_http_server(exposed_port)
    consumer = KafkaHandler()
    print(welcome_message)
    sentry_sdk.capture_message(welcome_message)
    for message in consumer.consume_loop():
        try:
            headers = {k: v.decode('utf-8')
                       for k, v in dict(message.headers()).items()}
            headers['service'] = service
            headers['topic'] = message.topic()
        except Exception as e:
            print("ERROR: ", e)
            sentry_sdk.set_context("message-headers", message.headers())
            sentry_sdk.capture_exception(e)
        finally:
            consumer.try_commit()
            try:
                counter.labels(**headers).inc()
            except Exception as e:
                print("ERROR: Error in mapping headers to configured ones", e)
                sentry_sdk.set_context("prometheus-labels", headers)
                sentry_sdk.capture_exception(e)
