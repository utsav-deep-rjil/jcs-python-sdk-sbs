import os
from ..common import utils
from ..common import log
from ..common.config_reader import ConfigReader


LOG = log.get_global_logger()

class Credentials(object):
    
    def __init__(self,access_key=None,secret_key=None):
        self._access_key = access_key
        self._secret_key = secret_key
        self._config = ConfigReader().config
        if self._config != None:
            self._env = self._config.get('branch','env')

    @property
    def access_key(self):
        """JCS ACCESS KEY"""
        if self._access_key == None:
            if "ACCESS_KEY" in os.environ:
                LOG.info("Using ACCESS_KEY from os environment variables")
                self._access_key = os.environ.get("ACCESS_KEY")
            elif self._config != None:
                self._access_key = self._config.get(self._env,'ACCESS_KEY')
                if self._access_key != None:
                    LOG.info("Using ACCESS_KEY from 'config.properties' file")
                else:
                    LOG.error("Unable to find ACCESS_KEY. (access_key is None)")
        return self._access_key

    @access_key.setter
    def access_key(self, value):
        self._access_key = utils.validate_string(value, "access_key")

    @access_key.deleter
    def access_key(self):
        del self._access_key
        
    @property
    def secret_key(self):
        """JCS SECRET KEY"""
        if self._secret_key == None:
            if "SECRET_KEY" in os.environ:
                LOG.info("Using SECRET_KEY from os environment variables")
                self._secret_key = os.environ.get("SECRET_KEY")
            elif self._config != None:
                self._secret_key = self._config.get(self._env,'SECRET_KEY')
                if self._secret_key != None:
                    LOG.info("Using SECRET_KEY from 'config.properties' file")
                else:
                    LOG.error("Unable to find SECRET_KEY. (secret_key is None)")
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = utils.validate_string(value, "secret_key")

    @secret_key.deleter
    def secret_key(self):
        del self._secret_key
        
        
        
        