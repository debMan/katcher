import random
import time

import prometheus_client as prom
from easycli import Root, Argument

#req_summary = prom.Summary('req_example', 'Time spent processing a request')
#
#
#@req_summary.time()
#def process_request(t):
#   time.sleep(t)

if __name__ == '__main__':

   counter = prom.Counter('counter', 'This is my counter')
   gauge = prom.Gauge('gauge', 'This is my gauge')
   histogram = prom.Histogram('histogram', 'This is my histogram')
   summary = prom.Summary('summary', 'This is my summary')
   prom.start_http_server(8080)

   while True:
       counter.inc(random.random())
       gauge.set(random.random() * 15 - 5)
       histogram.observe(random.random() * 10)
       summary.observe(random.random() * 10)
       #process_request(random.random() * 5)

       time.sleep(1)
