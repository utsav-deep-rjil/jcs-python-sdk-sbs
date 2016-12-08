from jcs_result import JCSResult
from ..common import utils

class DeleteVolumeResult(JCSResult):
    def __init__(self):
        self._deleted = None
        super(DeleteVolumeResult, self).__init__()

    @property
    def deleted(self):
        """Boolean value indicating if volume is deleted or not."""
        return self._deleted

    @deleted.setter
    def deleted(self, value):
        self._deleted = utils.validate_generic(value, "deleted", bool)

    @deleted.deleter
    def deleted(self):
        del self._deleted
    
    def __str__(self):
        return '{"deleted":"%s","request_id":"%s"}' % (self.deleted, self.request_id)
