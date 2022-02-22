from os import path, getenv
import yaml


class Config:

    """
    A simple handler for kafka configurations. The methods of this are used to
    handle config properties used to configure kafka client
    """

    def __init__(self, config_file="config.yml"):
        """
        :type topics: list
        :type config_file: str
        :arg topics:
            Containing list of the topics to be read
        :arg config_file:
            Containing the file path to config file
        """

        # The configuration is set in a yml file.
        dirname = path.dirname(path.abspath(__file__))
        absolute_path = str(dirname + "/" + config_file)
        self.config_file = getenv("CONFIG_ADDRESS", absolute_path)
        with open(self.config_file, "r") as ymlfile:
            config = yaml.safe_load(ymlfile)
        self.service = config["service"]
        self.counter_name = config["counter_name"]
        self.topics = config["topics"]
        self.consumer = config["consumer"]
        self.address = config["address"]
        self.header_fields = config["header_fields"]
        self.timeout = config.get("timeout", 6000)
        self.offset_reset = config.get("offset_reset", "earliest")
        self.port = config.get("port", 80)
        if config.get("sentry", None) is not None:
            self.sentry = config.get("sentry")
            self.sentry["dsn"] = self.sentry.get("dsn", None)
            self.sentry["release"] = self.sentry.get("release", None)
            self.sentry["environment"] = self.sentry.get(
                "environment", "production")
            self.sentry["send-default-pii"] = self.sentry.get(
                "send-default-pii", False)
            self.sentry["debug"] = self.sentry.get("debug", False)
            self.sentry["traces-sample-rate"] = self.sentry.get(
                "traces-sample-rate", 1.0)
        else:
            self.sentry = None
