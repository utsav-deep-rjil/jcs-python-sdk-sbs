from snapshot import Snapshot
from ..common import utils
from jcs_result import JCSResult

class CreateSnapshotResult(JCSResult):
    """
    Response class for create snapshot operation.
    
    Attributes:
        snapshot (:class:`jcs_sbs_sdk.model.snapshot.Snapshot`): Object of the class Snapshot that contains details of the created snapshot.
    """
    def __init__(self):
        self._snapshot = None
        super(CreateSnapshotResult, self).__init__()

    @property
    def snapshot(self):
        """(:class:`jcs_sbs_sdk.model.Snapshot`) Object of the created snapshot."""
        return self._snapshot

    @snapshot.setter
    def snapshot(self, value):
        self._snapshot = utils.validate_generic(value, "snapshot", type(Snapshot()))

    @snapshot.deleter
    def snapshot(self):
        del self._snapshot
    
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        return '{"snapshot":%s,"request_id":"%s"}' % (self.snapshot.__str__(), self.request_id)
