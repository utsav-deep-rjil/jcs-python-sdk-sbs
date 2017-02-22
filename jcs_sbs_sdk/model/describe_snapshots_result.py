from snapshot import Snapshot
from ..common import utils
from jcs_result import JCSResult

class DescribeSnapshotsResult(JCSResult):
    """
    Response class for the describe snapshots operation.
    
    Attributes:
        snapshots (:obj:`list` of :class:`jcs_sbs_sdk.model.snapshot.Snapshot`): List of Snapshot objects that contain results of the describe snapshots operation.
    """
    def __init__(self):
        self._snapshots = None
        super(DescribeSnapshotsResult, self).__init__()

    @property
    def snapshots(self):
        """(:obj:`list` of :class:`jcs_sbs_sdk.model.snapshot.Snapshot`) List of snapshot objects."""
        return self._snapshots

    @snapshots.setter
    def snapshots(self, value):
        self._snapshots = utils.validate_list(value, "snapshots", type(Snapshot()))

    @snapshots.deleter
    def snapshots(self):
        del self._snapshots
    
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        snapshots_str = []
        for snapshot in self.snapshots:
            snapshots_str.append(snapshot.__str__())
        snapshots_str = ",".join(snapshots_str)
        snapshots_str = "[%s]"%snapshots_str
        to_string = '{"snapshots":%s,"request_id":"%s"}' % (snapshots_str, self.request_id)
        return to_string#.replace("'", "")
