from datetime import datetime

from ..common import utils

class Snapshot:
    """
    Model class for a snapshot.
    
    Attributes:
        volume_id (:obj:`str`): ID of the volume from which the snapshot is created.
        
        volume_size (positive :obj:`int`): Size of the source volume.
        
        snapshot_id (:obj:`str`): ID of the snapshot.
        
        encrypted (:obj:`bool`): Indicates if the snapshot is encrypted or not.
        
        status (:obj:`str`): Current status of the snapshot. Possible values are: *pending*, *completed* and *error*.
        
        start_time (:obj:`datetime`): The datetime value at the which snapshot is created.
    """
    def __init__(self):
        self._volume_id = None
        self._volume_size = None
        self._snapshot_id = None
        self._encrypted = None
        self._status = None
        self._start_time = None

    @property
    def volume_id(self):
        """(:obj:`str`) ID of the volume from which the snapshot gets created."""
        return self._volume_id

    @volume_id.setter
    def volume_id(self, value):
        self._volume_id = utils.validate_string(value, "volume_id")

    @volume_id.deleter
    def volume_id(self):
        del self._volume_id
        
    @property
    def volume_size(self):
        """(positive :obj:`int`) Size of the source volume."""
        return self._volume_size

    @volume_size.setter
    def volume_size(self, value):
        self._volume_size = utils.validate_positive_int(value, "volume_size")

    @volume_size.deleter
    def volume_size(self):
        del self._volume_size
    
    @property
    def snapshot_id(self):
        """(:obj:`str`) ID of the snapshot."""
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = utils.validate_string(value, "volume_type")

    @snapshot_id.deleter
    def snapshot_id(self):
        del self._snapshot_id
    
    @property
    def encrypted(self):
        """(:obj:`bool`) Indicates if the snapshot is encrypted or not."""
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value):
        self._encrypted = utils.validate_generic(value, "encrypted", bool)

    @encrypted.deleter
    def encrypted(self):
        del self._encrypted
    
    @property
    def status(self):
        """(:obj:`str`) Current status of the snapshot. Possible values are: *pending*, *completed* and *error*."""
        return self._status

    @status.setter
    def status(self, value):
        self._status = utils.validate_string(value, "status")

    @status.deleter
    def status(self):
        del self._status
        
    @property
    def start_time(self):
        """(:obj:`datetime`) Time at which the snapshot is created."""
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = utils.validate_generic(value, "start_time", type(datetime))

    @start_time.deleter
    def start_time(self):
        del self._start_time
        
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        to_string = '{"volume_id":"%s","volume_size":%s,"snapshot_id":"%s","encrypted":"%s","status":"%s","start_time":"%s"}'%\
     (self.volume_id, self.volume_size, self.snapshot_id, self.encrypted, self.status, str(self.start_time))
        to_string = to_string.replace('"None"', "null")
        to_string = to_string.replace("None", "null")
        return to_string

