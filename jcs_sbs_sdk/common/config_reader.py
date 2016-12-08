import ConfigParser, os

import log


LOG = log.get_global_logger()

class ConfigReader(object):
    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        if os.path.exists("../../fixtures/config.properties"):
            self.config.read("../../fixtures/config.properties")
        else:
            LOG.warn("fixtures/config.properties not found")