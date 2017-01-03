from jcs_request import JCSRequest
from ..common import utils

class DeleteSnapshotRequest(JCSRequest):
    """
    Request class for delete snapshot operation.
    
    Attributes:
        snapshot_id (str): ID of the snapshot to be deleted.
    """
    def __init__(self):
        self._snapshot_id = None
        super(DeleteSnapshotRequest, self).__init__()

    @property
    def snapshot_id(self):
        """ID of the snapshot to be deleted (string)."""
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = utils.validate_string(value, "snapshot_id")

    @snapshot_id.deleter
    def snapshot_id(self):
        del self._snapshot_id

    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        return '{"snapshot_id":"%s"}' % (self.snapshot_id)