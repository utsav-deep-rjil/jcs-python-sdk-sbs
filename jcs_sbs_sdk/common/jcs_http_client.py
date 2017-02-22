import os
import urllib2

import utils
import log

from ..auth.authorization import Authorization
from ..auth.credentials import Credentials


LOG = log.get_global_logger()

class JCSHttpClient(object):
    """
    Contains methods required for making requests to backend APIs and relevant utility methods.
    The methods of this class are used internally.
    
    The constructor of this class takes optional argument, 'base_url', as defined in Args.
        
    Args:
        base_url (str,optional, default = None): The base URL of the backend API.
    
    Attributes:
        endpoint (:obj:`str`): The base URL of the backend API.
        
        _config (:class:`ConfigParser`): An object of :class:`ConfigParser` returned by the :func:`jcs_sbs_sdk.common.utils.get_config` method.
        
        _env (:obj:`str`): If _config is not None, _env contains the branch name
    """
    def __init__(self, base_url=None):
        self._endpoint = base_url
        self._config = utils.get_config()
        if self._config != None:
            self._env = self._config.get('branch','env')
        
    
    @property
    def endpoint(self):
        """(:obj:`str`) Base URL of the internal API"""
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
            headers(:obj:`dict`): Mapped header values required in the URL of the internal API calls
        
        Raises:
            TypeError: If *headers* is not of type :obj:`dict`
        """
        utils.validate_generic(headers, "headers", type({}))
        headers["Content-Type"] = "application/json"
        headers["Accept-Encoding"] = "identity"
    
    
    def get_url(self, query_params):
        """
        Generates and returns the URL string after adding the query parameters to it.
        
        Args:
            query_params (:obj:`dict`): Query parameters to add to the API request.
            
        Returns:
            (:obj:`str`) URL encoded string containing the values from the passed query parameters.
        
        Raises:
            TypeError: If *query_params* is not a :obj:`dict`.
        """
        utils.validate_generic(query_params, "query_params", type({}))
        encoded_params = []
        for key in list(query_params):
            encoded_params.append("=".join([key,str(query_params.get(key))]))
        return "/?".join([self.endpoint, "&".join(encoded_params)])
    
    
    def make_request(self, credentials, query_params, headers, request_method):
        """
        Generates the final API URL, calls the API and returns the HTTP response object that contains the backend API response. 
        
        Args:
            credentials (:class:`jcs_sbs_sdk.auth.credentials.Credentials`): An object of the class Credentials that contains values of ACCESS_KEY and
                SECRET_KEY
            query_params (:obj:`dict`): Query parameters to add to the API request.
            
            headers (:obj:`dict`): Headers required in the API call.
            
        Returns:
            (:obj:`response`) The response object that contains the details of the API response.
                     
        Raises:
            TypeError: If:
                * *credentials* is not an object of :class:`jcs_sbs_sdk.auth.credentials.Credentials`
                * *query_params* and *headers* are not of type :obj:`dict`
                * *request_method* is not of type :obj:`str`
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
