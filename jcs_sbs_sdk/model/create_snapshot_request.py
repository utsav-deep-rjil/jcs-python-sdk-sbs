from ..common import utils
from jcs_request import JCSRequest

class CreateSnapshotRequest(JCSRequest):
    """
    Request class for create snapshot operation.
    
    Attributes:
        volume_id (str): ID of volume from which the snapshot is to be created.
    """
    def __init__(self):
        self._volume_id = None
        super(CreateSnapshotRequest, self).__init__()

    @property
    def volume_id(self):
        """ID of volume from which the snapshot is to be created."""
        return self._volume_id

    @volume_id.setter
    def volume_id(self, value):
        self._volume_id = utils.validate_string(value, "volume_id")

    @volume_id.deleter
    def volume_id(self):
        del self._volume_id
    
    def __str__(self):
        to_string = '{"volume_id":"%s"}'%(self.volume_id)
        to_string = to_string.replace('"None"', "null")
        return to_string