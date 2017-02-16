from ..auth.credentials import Credentials
from ..common import utils
    
class JCSRequest(object):
    """
    Parent class for all the request classes. Contains the common attributes for all the requests.
    
    Attributes:
        credentials (:obj:`jcs_sbs_sdk.auth.credentials.Credentials`): An object of the Credentials class that contains access and secret keys,
            that are required for sending any request.
        
        custom_request_headers (:obj:`dict`): Stores some custom headers in a :obj:`dict`, required to send any request to the internal APIs.
    """
    def __init__(self):
        self._credentials = None
        self._custom_request_headers = {}
    
    @property
    def credentials(self):
        """(:obj:`jcs_sbs_sdk.auth.credentials.Credentials`) Credentials object containing the ACCESS_KEY and the SECRET_KEY."""
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._request_id = utils.validate_generic(value, "credentials", type(Credentials()))

    @credentials.deleter
    def credentials(self):
        del self._credentials
        
    @property
    def custom_request_headers(self):
        """(:obj:`dict`) Custom headers required to send any request to the internal APIs"""
        return self._custom_request_headers

    @custom_request_headers.setter
    def custom_request_headers(self, value):
        self._custom_request_headers = utils.validate_generic(value, "custom_request_headers", dict)

    @custom_request_headers.deleter
    def custom_request_headers(self):
        del self._custom_request_headers
