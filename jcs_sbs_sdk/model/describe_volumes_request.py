from ..common import utils
from jcs_request import JCSRequest

class DescribeVolumesRequest(JCSRequest):
    """
    Request class for describe volumes operation.
    
    Attributes:
        volume_ids (list of str): IDs of specific volume to be described.
        
        next_token (str): ID of last volume in the previous call of describe_volume method.
            If the describeVolumes() method was called with a MaxResults option,
            all items would not have been returned. So, the previous call of
            describeVolumes() method returns 'nextToken' to get next set of items.
            This is basically the Id of the last seen item from the previous call.
            The describeVolumes() will return the next set of items after this Id
            and the new value of 'nextToken'
            
        max_results (int): Maximum number of volumes to be described.
            To get the next set of volumes, ID of the last volume should be passed as 'next_token'
            in next call of describe volume.
        
        detail (bool): If 'detail' is set to 'True', then the volumes will be described in detail.
    """
    def __init__(self):
        self._volume_ids = None
        self._next_token = None
        self._max_results = None
        self._detail = None
        super(DescribeVolumesRequest, self).__init__()

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
        """
        Returns JSON string representation of this class used for debugging.
        """
        to_string = '{"volume_ids":"%s","next_token":"%s","max_results":"%s","detail":"%s"}'\
        % (str(self.volume_ids), self.next_token, self.max_results, self.detail)
        to_string = to_string.replace('"None"', "null")
        to_string = to_string.replace("None", "null")
        return to_string
    
