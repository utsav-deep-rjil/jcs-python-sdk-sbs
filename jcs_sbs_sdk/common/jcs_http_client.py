import os
import urllib2

import utils
import log
from config_reader import ConfigReader

from ..auth.authorization import Authorization
from ..auth.credentials import Credentials


LOG = log.get_global_logger()

class JCSHttpClient(object):
    
    def __init__(self, base_url=None):
        self._endpoint = base_url
        self._config = ConfigReader().config
        if self._config != None:
            self._env = self._config.get('branch','env')
        
    
    @property
    def endpoint(self):
        """Base URL of internal APIs"""
        if self._endpoint == None:
            if "BASE_URL" in os.environ:
                LOG.info("Using BASE_URL from OS environment variables")
                self._endpoint = os.environ.get("BASE_URL")
            elif self._config != None:
                self._endpoint = self._config.get(self._env,'BASE_URL')
                if self._endpoint != None:
                    LOG.info("Using BASE_URL: %s from 'config.properties' file",self._endpoint)
                else:
                    LOG.error("Unable to find BASE_URL. (endpoint is None)")
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = utils.validate_string(value, "endpoint")
        
    def add_custom_headers(self, headers):
        utils.validate_generic(headers, "headers", type({}))
        headers["Content-Type"] = "application/json"
        headers["Accept-Encoding"] = "identity"
    
    def get_url(self, query_params):
        utils.validate_generic(query_params, "query_params", type({}))
        encoded_params = []
        for key in list(query_params):
            encoded_params.append("=".join([key,str(query_params.get(key))]))
        return "/?".join([self.endpoint, "&".join(encoded_params)])
    
    def make_request(self, credentials, query_params, headers, request_method):
        utils.validate_generic(credentials, "credentials", Credentials)
        utils.validate_generic(query_params, "query_params", type({}))
        utils.validate_generic(headers, "headers", type({}))
        utils.validate_string(request_method, "request_method")
        
        self.add_custom_headers(headers)
        auth = Authorization(self.endpoint, request_method, credentials, headers)
        auth.add_auth(query_params)
        url = self.get_url(query_params)
        LOG.info("Getting response from URL: %s", url)
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        return response
