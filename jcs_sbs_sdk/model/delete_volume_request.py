from jcs_request import JCSRequest
from ..common import utils

class DeleteVolumeRequest(JCSRequest):
    """
    Request class for the delete volume operation.
    
    Attributes:
        volume_id (:obj:`str`): ID of the volume to delete.
    """
    def __init__(self):
        self._volume_id = None
        super(DeleteVolumeRequest, self).__init__()

    @property
    def volume_id(self):
        """(:obj:`str`) ID of the volume to delete."""
        return self._volume_id

    @volume_id.setter
    def volume_id(self, value):
        self._volume_id = utils.validate_string(value, "volume_id")

    @volume_id.deleter
    def volume_id(self):
        del self._volume_id
    
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        return '{"volume_id":"%s"}' % (self.volume_id)