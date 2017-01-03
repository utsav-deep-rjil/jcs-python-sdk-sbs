import os
import urllib2

import utils
import log

from ..auth.authorization import Authorization
from ..auth.credentials import Credentials


LOG = log.get_global_logger()

class JCSHttpClient(object):
    """
    Contains methods required for making requests to backend APIs and some other methods used internally.
    The constructor takes optional argument, 'base_url', as defined in Args.
        
    Args:
        base_url (str,optional, default = None): The base URL of the backend API.
    
    Attributes:
        endpoint (str): The base URL of the backend API.
        
        _config (ConfigParser): An instance of ConfigParser object as returned by 'utils.get_config()' method.
        
        _env (str): If _config is not None, _env contains the branch name
    """
    def __init__(self, base_url=None):
        self._endpoint = base_url
        self._config = utils.get_config()
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
        """
        Adds custom headers that are required to send backend API request.
        
        Args:
            headers(dict): mapped header values required in the URL of the API calls
        
        Raises:
            TypeError: If 'headers' is not of type 'dict'
        """
        utils.validate_generic(headers, "headers", type({}))
        headers["Content-Type"] = "application/json"
        headers["Accept-Encoding"] = "identity"
    
    def get_url(self, query_params):
        """
        Generates and returns the URL string after adding the query parameters to it.
        
        Args:
            query_params(dict): Query parameters to be added in the API being called.
            
        Returns:
            URL encoded string containing the values from passed query parameters.
        
        Raises:
            TypeError: If 'query_params' is not a 'dict'.
        """
        utils.validate_generic(query_params, "query_params", type({}))
        encoded_params = []
        for key in list(query_params):
            encoded_params.append("=".join([key,str(query_params.get(key))]))
        return "/?".join([self.endpoint, "&".join(encoded_params)])
    
    def make_request(self, credentials, query_params, headers, request_method):
        """
        Generates final API URL, calls it and returns the HTTP response object
        containing the response returned by backend API.
        
        Args:
            credentials: Object of type JCSCredentials, contains ACCESS_KEY and
                 SECRET_KEY
            query_params: Query Params in the API call
            
            headers: Headers to be present in the API call
            
        Returns:
            'response' object is returned containing the details of the response returned by the API.
            
        Raises:
            TypeError: If:
                'credentials' is not an instance of class 'Credentials'
                'query_params' and 'headers' are not of type 'dict'
                'request_method' is not of type 'string'
     
        """
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
