from volume import Volume
from ..common import utils
from jcs_result import JCSResult

class CreateVolumeResult(JCSResult):
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
        return '{"volume":%s,"request_id":"%s"}' % (self.volume.__str__(), self.request_id)
