from ..common import utils
from attachment import Attachment
from datetime import datetime

class Volume:
    """
    Model class for a volume.
    
    Attributes:
        volume_id (:obj:`str`): ID of the volume.
        
        size (positive :obj:`int`): Size of the volume.
        
        volume_type (:obj:`str`): Type of the volume. Possible values are 'standard' or 'ms1'
        
        snapshot_id (:obj:`str`): ID of snapshot (if any) from which the volume is created.
        
        encrypted (:obj:`bool`): Indicates if the volume is encrypted or not.
        
        status (:obj:`str`): Current status of the volume. Possible values are: 'creating', 'available', 'in-use' and 'error'.
        
        attachments (:obj:`list` of :obj:`jcs_sbs_sdk.model.attachment.Attachment`): List of the devices to which this volume is attached.
        
        create_time (:obj:`datetime`): The *datetime* value at which the volume is created.
    """
    def __init__(self):
        self._volume_id = None
        self._size = None
        self._volume_type = None
        self._snapshot_id = None
        self._encrypted = None
        self._status = None
        self._attachments = None
        self._create_time = None

    @property
    def volume_id(self):
        """(:obj:`str`) ID of the volume"""
        return self._volume_id

    @volume_id.setter
    def volume_id(self, value):
        self._volume_id = utils.validate_string(value, "volume_id")

    @volume_id.deleter
    def volume_id(self):
        del self._volume_id
        
    @property
    def size(self):
        """(positive :obj:`int`) Size of the volume"""
        return self._size

    @size.setter
    def size(self, value):
        self._size = utils.validate_positive_int(value, "size")

    @size.deleter
    def size(self):
        del self._size
    
    @property
    def volume_type(self):
        """(:obj:`str`) Type of the volume. The types can be 'standard' or 'ms1'."""
        return self._volume_type

    @volume_type.setter
    def volume_type(self, value):
        self._volume_type = utils.validate_string(value, "volume_type")

    @volume_type.deleter
    def volume_type(self):
        del self._volume_type
    
    @property
    def snapshot_id(self):
        """(:obj:`str`) ID of snapshot (if any) from which the volume is created. """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = utils.validate_string(value, "volume_type")

    @snapshot_id.deleter
    def snapshot_id(self):
        del self._snapshot_id
    
    @property
    def encrypted(self):
        """(:obj:`bool`) Indicates if the volume is encrypted or not."""
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value):
        self._encrypted = utils.validate_generic(value, "encrypted", bool)

    @encrypted.deleter
    def encrypted(self):
        del self._encrypted
    
    @property
    def status(self):
        """(:obj:`str`) Current status of the volume. Possible values are: 'creating', 'available', 'in-use' and 'error'."""
        return self._status

    @status.setter
    def status(self, value):
        self._status = utils.validate_string(value, "status")

    @status.deleter
    def status(self):
        del self._status
        
    @property
    def attachments(self):
        """(:obj:`list` of :obj:`jcs_sbs_sdk.model.attachment.Attachment`) List of the devices to which this volume is attached.."""
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        self._attachments = utils.validate_list(value, "attachments", type(Attachment()))

    @attachments.deleter
    def attachments(self):
        del self._attachments
        
    @property
    def create_time(self):
        """(:obj:`datetime`) Time at which the volume is created."""
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = utils.validate_generic(value, "create_time", type(datetime))

    @create_time.deleter
    def create_time(self):
        del self._create_time
        
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        attachment_str = []
        for attachment in self.attachments:
            attachment_str.append(attachment.__str__())
        attachment_str = ",".join(attachment_str)
        attachment_str = "[%s]"%attachment_str
        to_string = '{"volume_id":"%s","size":%d,"volume_type":"%s","snapshot_id":"%s","encrypted":"%s","status":"%s","attachments":%s,"create_time":"%s"}'%\
     (self.volume_id, self.size, self.volume_type, self.snapshot_id, self.encrypted, self.status, attachment_str, str(self.create_time))
        to_string = to_string.replace('"None"', "null")
        to_string = to_string.replace("None", "null")
        return to_string#.replace("'", "")

