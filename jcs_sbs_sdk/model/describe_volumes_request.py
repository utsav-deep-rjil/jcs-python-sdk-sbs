from ..common import utils
from jcs_request import JCSRequest

class DescribeVolumesRequest(JCSRequest):
    def __init__(self):
        self._volume_ids = None
        self._next_token = None
        self._max_results = None
        self._detail = None
        super(DescribeVolumesRequest,self).__init__()

    @property
    def volume_ids(self):
        """List of volume IDs (string)."""
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, value):
        self._volume_ids = utils.validate_list(value, "volume_id", str)

    @volume_ids.deleter
    def volume_ids(self):
        del self._volume_ids
        
    @property
    def next_token(self):
        """Last volume Id (string) returned by previous call of describe_volume method. """
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = utils.validate_string(value, "next_token")

    @next_token.deleter
    def next_token(self):
        del self._next_token
    
    @property
    def max_results(self):
        """Maximum number of volumes to be described"""
        return self._max_results

    @max_results.setter
    def max_results(self, value):
        self._max_results = utils.validate_generic(value, "max_results", int)

    @max_results.deleter
    def max_results(self):
        del self._max_results
    
    @property
    def detail(self):
        """Boolean value indicating if details will be shown in response or not."""
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = utils.validate_generic(value, "detail", bool)

    @detail.deleter
    def detail(self):
        del self._detail
        
    def __str__(self):
        to_string = '{"volume_ids":"%s","next_token":"%s","max_results":"%s","detail":"%s"}'\
        % (str(self.volume_ids),self.next_token,self.max_results,self.detail)
        to_string = to_string.replace('"None"', "null")
        return to_string
    
