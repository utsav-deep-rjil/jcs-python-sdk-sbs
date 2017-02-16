from ..common import utils
from jcs_request import JCSRequest

class DescribeSnapshotsRequest(JCSRequest):
    """
    Request class for the describe snapshots operation.
    
    Attributes:
        snapshot_ids (:obj:`list` of :obj:`str`): IDs of specific snapshots to describe.
        
        next_token (:obj:`str`): ID of the last snapshot in the previous call of the describe_snapshots() method.
            Previously, if the describe_snapshots() method is called with 'max_results' option, all items are not returned.
            To get the next set of snapshots, pass the ID of the last snapshot as 'next_token' in the subsequent call to the describe_snapshots() method.
            
        max_results (:obj:`int`): Maximum number of snapshots to describe.
            To get the next set of snapshots, pass the ID of the last snapshot as 'next_token' in the subsequent call to the describe_snapshots() method.
            
        detail (:obj:`bool`): Set *True* to describe the snapshots in detail.
    """
    def __init__(self):
        self._snapshot_ids = None
        self._next_token = None
        self._max_results = None
        self._detail = None
        super(DescribeSnapshotsRequest, self).__init__()

    @property
    def snapshot_ids(self):
        """(:obj:`list` of :obj:`str`) List of the snapshot IDs."""
        return self._snapshot_ids

    @snapshot_ids.setter
    def snapshot_ids(self, value):
        self._snapshot_ids = utils.validate_list(value, "snapshot_id", str)

    @snapshot_ids.deleter
    def snapshot_ids(self):
        del self._snapshot_ids
        
    @property
    def next_token(self):
        """(:obj:`str`) ID of the last snapshot that is returned by the previous call of the describe_snapshot() method."""
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = utils.validate_string(value, "next_token")

    @next_token.deleter
    def next_token(self):
        del self._next_token
    
    @property
    def max_results(self):
        """(:obj:`int`) Maximum number of snapshots to describe."""
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
        to_string = '{"snapshot_ids": %s,"next_token":"%s","max_results":"%s","detail":"%s"}'\
             % (str(self.snapshot_ids), self.next_token, self.max_results, self.detail)
        to_string = to_string.replace('"None"', "null")
        to_string = to_string.replace("None", "null")
        return to_string.replace("'", '"')
    
