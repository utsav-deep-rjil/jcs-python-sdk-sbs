from ..common import utils

class JCSResult(object):
    """
    Parent class for all the result classes. Contains common attributes present in any result class.
    
    Attributes:
        request_id (:obj:`str`): Request ID returned by the internal API.
        
        xml (:obj:`str`): Actual XML response returned by the internal API.
    """
    def __init__(self):
        self._request_id = None
        self._xml = None

    @property
    def request_id(self):
        """(:obj:`str`) The ID of the request sent to the internal API."""
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = utils.validate_string(value, "request_id")

    @request_id.deleter
    def request_id(self):
        del self._request_id
        
    @property
    def xml(self):
        """(:obj:`str`) XML response returned by the internal API"""
        return self._xml

    @xml.setter
    def xml(self, value):
        self._xml = utils.validate_string(value, "xml")

    @xml.deleter
    def xml(self):
        del self._xml