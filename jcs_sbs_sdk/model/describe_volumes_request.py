from ..common import utils
from jcs_request import JCSRequest

class DescribeVolumesRequest(JCSRequest):
    """
    Request class for describe volumes operation.
    
    Attributes:
        volume_ids (:obj:`list` of :obj:`str`): IDs of specific volume to be described.
        
        next_token (:obj:`str`): ID of last volume in the previous call of the describe_volumes() method.
            Previously, if the describe_volumes() method is called with 'max_results' option, all items are not returned.
            To get the next set of volumes, pass the ID of the last volume as 'next_token' in the subsequent call to the describe_volumes() method.
            
        max_results (:obj:`int`): Maximum number of volumes to describe.
            To get the next set of volumes, pass the ID of the last volume as 'next_token' in the subsequent call to the describe_volumes() method.
        
        detail (:obj:`bool`): Set *True* to describe the snapshots in detail.
    """
    def __init__(self):
        self._volume_ids = None
        self._next_token = None
        self._max_results = None
        self._detail = None
        super(DescribeVolumesRequest, self).__init__()

    @property
    def volume_ids(self):
        """(:obj:`list` of :obj:`str`) List of volume IDs."""
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, value):
        self._volume_ids = utils.validate_list(value, "volume_id", str)

    @volume_ids.deleter
    def volume_ids(self):
        del self._volume_ids
        
    @property
    def next_token(self):
        """(:obj:`str`) ID of the last volume returned by the previous call of the describe_volumes() method. """
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = utils.validate_string(value, "next_token")

    @next_token.deleter
    def next_token(self):
        del self._next_token
    
    @property
    def max_results(self):
        """(:obj:`int`) Maximum number of volumes to describe."""
        return self._max_results

    @max_results.setter
    def max_results(self, value):
        self._max_results = utils.validate_generic(value, "max_results", int)

    @max_results.deleter
    def max_results(self):
        del self._max_results
    
    @property
    def detail(self):
        """(:obj:`bool`) Set *True* to describe the snapshots in detail."""
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
    
