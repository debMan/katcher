# Kafka header counter for prometheus

This simple script developed in order to count a specefic header values from
kafka messages. For example, we are going to count the messages fetched by
individual user IDs by twitter crawler.

## Configurations

A sample config file provided in `config.example.yml`. It's **required** to
mount a config file inside the cotainer with the name `config.yml` at
`/app/config.yml` or provide the config file absoulte path with environment
variable `CONFIG_ADDRESS`.

### config example

``` yaml
## Required configs ##
## just name the service for exported descriptions
service: example_service
## counter name for exported metrics
counter_name: test_counter_name
## kafka topics to fetch messages from
topics:
  - test_topic_a
  - test_topic_b
## consumer group name of this exporter
consumer: test_consumer_group
## a list of kafka addresses with port
address:
  - kafka.example.com:9092
## header name to fetch data from it
header_field: test_header_field

## Optional configs ##
## timeouts in ms
timeout: 6000
## offset reset policy, can be earliest or latest
offset_reset: earliest
## exposed http server port for prometheus scraper
port: 80
```

## Type

RESTful API

## Source

Apache kafka

## Output

Prometheus

## Tests

Not developed yet

## Deployment Notes

### Hardware Requirements

- Memory: 100 Mi - 128 Mi
- CPU: 0.7 - 1
- Storage: None
