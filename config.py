from os import path
import yaml


class Config:

    """
    A simple handler for configurations. The methods of this are used to handle
    environment variables which are configured for database and etc and some
    properties used to configure kafka client
    """

    def __init__(self, topics, config_file="config.yml"):
        """
        :type topics: list
        :type config_file: str
        :arg topics:
            Containing list of the topics to be read
        :arg config_file:
            Containing the file path to config file
        """

        self.topics = topics
        self.config_file = getenv("CONFIG_ADDRESS", default=config_file)

        # The configuration is set in a yml file.
        dirname = path.dirname(path.abspath(__file__))
        with open(str(dirname + "/" + config_file), "r") as ymlfile:
            config = yaml.safe_load(ymlfile)

        # All of the configuration is set in the conf attribute as dict
        self.conf = config[self.topics]
