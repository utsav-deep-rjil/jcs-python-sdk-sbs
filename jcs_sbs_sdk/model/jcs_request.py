from ..auth.credentials import Credentials
from ..common import utils
    
class JCSRequest(object):
    """
    Parent class for all the request classes. Contains the common attributes for all the requests.
    
    Attributes:
        credentials (Credentials): An instance of Credentials object containing access and secret keys,
            which is required for sending any request.
        
        custom_request_headers (dict): Stores some custom headers,
            required for sending any request to the backend API, in a dictionary.
    """
    def __init__(self):
        self._credentials = None
        self._custom_request_headers = {}
    
    @property
    def credentials(self):
        """Credentials object containing ACCESS_KEY and SECRET_KEY."""
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._request_id = utils.validate_generic(value, "credentials", type(Credentials()))

    @credentials.deleter
    def credentials(self):
        del self._credentials
        
    @property
    def custom_request_headers(self):
        """custom headers required for sending request to backend API"""
        return self._custom_request_headers

    @custom_request_headers.setter
    def custom_request_headers(self, value):
        self._custom_request_headers = utils.validate_generic(value, "custom_request_headers", dict)

    @custom_request_headers.deleter
    def custom_request_headers(self):
        del self._custom_request_headers
