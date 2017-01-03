from ..common import utils
from jcs_request import JCSRequest

class CreateVolumeRequest(JCSRequest):
    """
    Request class for create volume operation.
    
    Attributes:
        size (int): Size of the volume.
        snapshot_id (str): ID of snapshot from which the volume is to be created.
        volume_type (str): Type of the volume to be created. The types can be 'standard' or 'ms1' 
        encrypted (bool): Indicates if created volume will be encrypted or not.
    """
    def __init__(self):
        self._size = None
        self._snapshot_id = None
        self._volume_type = None
        self._encrypted = None
        super(CreateVolumeRequest, self).__init__()

    @property
    def size(self):
        """Size of the Volume (int)"""
        return self._size

    @size.setter
    def size(self, value):
        self._size = utils.validate_positive_int(value, "size")

    @size.deleter
    def size(self):
        del self._size
        
    @property
    def snapshot_id(self):
        """ID of snapshot from which the volume is to be created."""
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = utils.validate_string(value, "snapshot_id")

    @snapshot_id.deleter
    def snapshot_id(self):
        del self._snapshot_id
    
    @property
    def volume_type(self):
        """Type of the volume (str). The types can be 'standard' or 'ms1' """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, value):
        self._volume_type = utils.validate_string(value, "volume_type")

    @volume_type.deleter
    def volume_type(self):
        del self._volume_type
    
    @property
    def encrypted(self):
        """Boolean value indicating if volume is encrypted or not."""
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value):
        self._encrypted = utils.validate_generic(value, "encrypted", bool)

    @encrypted.deleter
    def encrypted(self):
        del self._encrypted
        
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        to_string = '{"size":%d,"volume_type":"%s","snapshot_id":"%s","encrypted":"%s"}'%\
        (self.size, self.volume_type, self.snapshot_id, self.encrypted)
        to_string = to_string.replace('"None"', "null")
        to_string = to_string.replace("None", "null")
        return to_string#.replace("'", "")
