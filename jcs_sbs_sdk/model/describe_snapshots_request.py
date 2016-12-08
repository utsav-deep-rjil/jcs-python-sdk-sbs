from ..common import utils
from jcs_request import JCSRequest
import json

class DescribeSnapshotsRequest(JCSRequest):
    def __init__(self):
        self._snapshot_ids = None
        self._next_token = None
        self._max_results = None
        self._detail = None
        super(DescribeSnapshotsRequest,self).__init__()

    @property
    def snapshot_ids(self):
        """List of snapshot IDs (string)."""
        return self._snapshot_ids

    @snapshot_ids.setter
    def snapshot_ids(self, value):
        self._snapshot_ids = utils.validate_list(value, "snapshot_id", str)

    @snapshot_ids.deleter
    def snapshot_ids(self):
        del self._snapshot_ids
        
    @property
    def next_token(self):
        """Last snapshot Id (string) returned by previous call of describe_snapshot method. """
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = utils.validate_string(value, "next_token")

    @next_token.deleter
    def next_token(self):
        del self._next_token
    
    @property
    def max_results(self):
        """Maximum number of snapshots to be described"""
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
        to_string = '{"snapshot_ids": %s,"next_token":"%s","max_results":"%s","detail":"%s"}'\
             % (str(self.snapshot_ids),self.next_token,self.max_results,self.detail)
        return to_string.replace("'", '"')
    
