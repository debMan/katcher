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

        self.config_file = getenv("CONFIG_ADDRESS", default=config_file)

        # The configuration is set in a yml file.
        dirname = path.dirname(path.abspath(__file__))
        with open(str(dirname + "/" + config_file), "r") as ymlfile:
            config = yaml.safe_load(ymlfile)
        self.topics = config["topics"]
        self.consumer = config["consumer"]
        self.address = config["address"]
        self.timeout = config["timeout"]
        self.offset_reset = config["offset_reset"]
        self.header_field = config["header_field"]
        self.service = config["service"]
        self.counter_name = config["counter_name"]