from ..common import utils

class Attachment(object):
    """
    Model class for storing information of the devices to which volume is attached.
    
    Attributes:
        instance_id (str): ID of instance to which the volume is attached.
        
        device (str): Device to which the volume is attached.
    """
    def __init__(self):
        self._instance_id = None
        self._device = None

    @property
    def instance_id(self):
        """ID of instance to which the volume is attached"""
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = utils.validate_string(value, "instance_id")

    @instance_id.deleter
    def instance_id(self):
        del self._instance_id
        
    @property
    def device(self):
        """Device to which the volume is attached"""
        return self._device

    @device.setter
    def device(self, value):
        self._device = utils.validate_string(value, "device")

    @device.deleter
    def device(self):
        del self._device
        
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        return '{"instance_id":"%s","device":"%s"}' % (self.instance_id, self.device)    
    
        
