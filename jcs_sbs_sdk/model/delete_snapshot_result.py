from jcs_result import JCSResult
from ..common import utils

class DeleteSnapshotResult(JCSResult):
    """
    Response class for delete snapshot operation.
    
    Attributes:
        deleted (bool): Indicates if the snapshot with given snapshot_id is deleted or not.
    """
    def __init__(self):
        self._deleted = None
        super(DeleteSnapshotResult, self).__init__()

    @property
    def deleted(self):
        """Boolean value indicating if snapshot is deleted or not."""
        return self._deleted

    @deleted.setter
    def deleted(self, value):
        self._deleted = utils.validate_generic(value, "deleted", bool)

    @deleted.deleter
    def deleted(self):
        del self._deleted
    
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        return '{"deleted":"%s","request_id":"%s"}' % (self.deleted, self.request_id)
