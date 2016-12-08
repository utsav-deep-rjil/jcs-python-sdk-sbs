from ..common import utils

class JCSResult(object):
    def __init__(self):
        self._request_id = None
        self._xml = None

    @property
    def request_id(self):
        """The ID of the request sent to the internal API."""
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = utils.validate_string(value, "request_id")

    @request_id.deleter
    def request_id(self):
        del self._request_id
        
    @property
    def xml(self):
        """XML response returned by internal API"""
        return self._xml

    @xml.setter
    def xml(self, value):
        self._xml = utils.validate_string(value, "xml")

    @xml.deleter
    def xml(self):
        del self._xml