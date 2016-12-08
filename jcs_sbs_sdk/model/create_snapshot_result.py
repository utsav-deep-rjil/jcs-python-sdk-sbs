from snapshot import Snapshot
from ..common import utils
from jcs_result import JCSResult

class CreateSnapshotResult(JCSResult):
    def __init__(self):
        self._snapshot = None
        super(CreateSnapshotResult, self).__init__()

    @property
    def snapshot(self):
        """Object of snapshot that is created"""
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        self._snapshot = utils.validate_generic(value, "snapshot", type(Snapshot()))

    @snapshot.deleter
    def snapshot(self):
        del self._snapshot
    
    def __str__(self):
        return '{"snapshot":%s,"request_id":"%s"}' % (self.snapshot.__str__(), self.request_id)
