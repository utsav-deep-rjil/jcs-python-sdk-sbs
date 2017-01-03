from volume import Volume
from ..common import utils
from jcs_result import JCSResult

class CreateVolumeResult(JCSResult):
    """
    Response class for create volume operation.
    
    Attributes:
        volume (Volume): An instance of volume class. Contains the details of the created volume.
    """
    def __init__(self):
        self._volume = None
        super(CreateVolumeResult, self).__init__()

    @property
    def volume(self):
        """Object of volume that is created"""
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = utils.validate_generic(value, "volumes", type(Volume()))

    @volume.deleter
    def volume(self):
        del self._volume
    
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        return '{"volume":%s,"request_id":"%s"}' % (self.volume.__str__(), self.request_id)
