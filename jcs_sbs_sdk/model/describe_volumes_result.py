from volume import Volume
from ..common import utils
from jcs_result import JCSResult

class DescribeVolumesResult(JCSResult):
    """
    Response class for describe volumes operation.
    
    Attributes:
        volumes (:obj:`list` of :class:`jcs_sbs_sdk.model.volume.Volume`): List of Volume objects that contain results of the describe snapshots operation.
    """
    def __init__(self):
        self._volumes = None
        super(DescribeVolumesResult, self).__init__()

    @property
    def volumes(self):
        """(:obj:`list` of :class:`jcs_sbs_sdk.model.volume.Volume`) List of volume objects"""
        return self._volumes

    @volumes.setter
    def volumes(self, value):
        self._volumes = utils.validate_list(value, "volumes", type(Volume()))

    @volumes.deleter
    def volumes(self):
        del self._volumes
    
    def __str__(self):
        """
        Returns JSON string representation of this class used for debugging.
        """
        volumes_str = []
        for volume in self.volumes:
            volumes_str.append(volume.__str__())
        volumes_str = ",".join(volumes_str)
        volumes_str = "[%s]"%volumes_str
        to_string = '{"volumes":%s,"request_id":"%s"}' % (volumes_str, self.request_id)
        return to_string#.replace("'", "")