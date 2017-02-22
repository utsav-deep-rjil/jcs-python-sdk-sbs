from datetime import datetime
from httplib import HTTPException
from lxml import objectify

from ..auth.credentials import Credentials
from ..common import constants
from ..common import utils
from ..common.jcs_http_client import JCSHttpClient
from ..model.attachment import Attachment
from ..model.create_snapshot_request import CreateSnapshotRequest
from ..model.create_snapshot_result import CreateSnapshotResult
from ..model.create_volume_request import CreateVolumeRequest
from ..model.create_volume_result import CreateVolumeResult
from ..model.delete_snapshot_request import DeleteSnapshotRequest
from ..model.delete_snapshot_result import DeleteSnapshotResult
from ..model.delete_volume_request import DeleteVolumeRequest
from ..model.delete_volume_result import DeleteVolumeResult
from ..model.describe_snapshots_request import DescribeSnapshotsRequest
from ..model.describe_snapshots_result import DescribeSnapshotsResult
from ..model.describe_volumes_request import DescribeVolumesRequest
from ..model.describe_volumes_result import DescribeVolumesResult
from ..model.snapshot import Snapshot
from ..model.volume import Volume


class JCSComputeClient(JCSHttpClient):
    """
    Contains methods that provide access to the operations supported by this SDK.
    The supported operations are create, describe and delete on volume and snapshot.
    
    Attributes:
        credentials (:class:`jcs_sbs_sdk.auth.credentials.Credentials`): Stores credentials (access and secret keys) 
            required for sending any backend API request.
            
    The init method takes following arguments:
    
    Args:
        credentials (:class:`jcs_sbs_sdk.auth.credentials.Credentials`, optional, default = None): Stores ACCESS_KEY and SECRET_KEY.
        
        base_url (:obj:`str`, optional, default = None): Base URL or endpoint for backend APIs.
    """
    def __init__(self, credentials=None, base_url=None):
        if credentials is None:
            credentials = Credentials()
        self._credentials = credentials
        super(JCSComputeClient, self).__init__(base_url)
        
        
    def describe_volumes(self, volume_ids=None, next_token=None, max_results=None, detail=None):
        """
        Returns an object of the :class:`jcs_sbs_sdk.model.describe_volumes_result.DescribeVolumesResult` containing the 
        :obj:`list` of :class:`jcs_sbs_sdk.model.volume.Volume` according to the corresponding internal API response.
        
        Args:
            volume_ids (:obj:`list` of :obj:`str`, optional, default = None): IDs of specific volume to be described.
            
            next_token (:obj:`str`, optional, default = None): ID of last volume in the previous call of the describe_volumes() method.
                Previously, if the describe_volumes() method is called with 'max_results' option, all items are not returned.
                To get the next set of volumes, pass the ID of the last volume as 'next_token' in the subsequent call to the describe_volumes() method.
                
            max_results (:obj:`int`, optional, default = None): Maximum number of volumes to describe.
                To get the next set of volumes, pass the ID of the last volume as 'next_token' in the subsequent call to the describe_volumes() method.
            
            detail (:obj:`bool`, optional, default = None): Set *True* to describe the snapshots in detail.
        
        Returns:
            An object of the :class:`jcs_sbs_sdk.model.describe_volumes_result.DescribeVolumesResult` containing the 
            :obj:`list` of :class:`jcs_sbs_sdk.model.volume.Volume` according to the corresponding internal API response.
        
        Raises:
            TypeError: If:
                * *volume_ids* is not a :obj:`list` of :obj:`str`
                * *next_token* is not of type :obj:`str`
                * *max_results* is not of type :obj:`int`
                * *detail* is not of type :obj:`bool`
        """
        
            
        describe_volumes_request = DescribeVolumesRequest()
        
        if volume_ids is not None:
            describe_volumes_request.volume_ids = volume_ids
            
        if next_token is not None:
            describe_volumes_request.next_token = next_token
            
        if max_results is not None:
            describe_volumes_request.max_results = max_results
            
        if detail is not None:
            describe_volumes_request.detail = detail
            
        query_params = {}
        query_params["Action"] = "DescribeVolumes"
        if describe_volumes_request.max_results != None:
            query_params["MaxResults"] = describe_volumes_request.max_results
        if describe_volumes_request.next_token != None:
            query_params["NextToken"] = describe_volumes_request.next_token
        if describe_volumes_request.detail != None:
            query_params["Detail"] = describe_volumes_request.detail
        if describe_volumes_request.volume_ids != None:
            for i, volume_id in enumerate(describe_volumes_request.volume_ids):
                query_params["VolumeId.%d" % (i + 1)] = volume_id
        
        response = self.make_request(self._credentials, query_params, describe_volumes_request.custom_request_headers, "GET")
        
        response_data = str(response.read())
        try:
            if response.code // 100 == 2:
                describe_volumes_response = objectify.fromstring(response_data)
                describe_volumes_result = DescribeVolumesResult()
                describe_volumes_result.request_id = str(describe_volumes_response.requestId)
                describe_volumes_result.volumes = []
                if hasattr(describe_volumes_response.volumeSet, "item"):
                    for volume_eo in describe_volumes_response.volumeSet.item:
                        volume = Volume()
                        volume.volume_id = str(volume_eo.volumeId)
                        volume.status = str(volume_eo.status)
                        if hasattr(volume_eo, "createTime"):
                            volume.create_time = datetime.strptime(str(volume_eo.createTime), constants.RESPONSE_DATE_TIME_FORMAT)
                        if hasattr(volume_eo, "size"):
                            volume.size = int(volume_eo.size)
                        if hasattr(volume_eo, "snapshotId"):
                            volume.snapshot_id = str(volume_eo.snapshotId)
                        if hasattr(volume_eo, "volumeType"):
                            volume.volume_type = str(volume_eo.volumeType)
                        if hasattr(volume_eo, "encrypted"):
                            volume.encrypted = volume_eo.encrypted
                        if hasattr(volume_eo, "attachmentSet"):
                            volume.attachments = []
                            if hasattr(volume_eo.attachmentSet, "item"):
                                for attachment_eo in volume_eo.attachmentSet.item:
                                    attachment = Attachment()
                                    attachment.device = str(attachment_eo.device)
                                    attachment.instance_id = str(attachment_eo.instanceId)
                                    volume.attachments.append(attachment)
                        describe_volumes_result.volumes.append(volume)
                describe_volumes_result.xml = response_data
                return describe_volumes_result
            else:
                raise HTTPException(response_data)
        finally:
            response.close()

    
    def create_volume(self, size=None, snapshot_id=None, volume_type=None, encrypted=None):
        """
        Creates a volume according to the arguments passed to this method and returns an object of :class:`jcs_sbs_sdk.model.create_volume_result.CreateVolumeResult`.
        
        Args:
            size (:obj:`int`, optional if *snapshot_id* is given, default = None): Size of the volume.
            
            snapshot_id (:obj:`str`, optional if *size* is given, default = None): ID of snapshot from which the volume gets created.
            
            volume_type (:obj:`str`, optional, default = None): Type of the volume, 'standard' or 'ms1', to create. 
            
            encrypted (:obj:`bool`, optional, default = None): Indicates if the volume that gets created is encrypted or not.
            
        Returns:
            An object of :class:`jcs_sbs_sdk.model.create_volume_result.CreateVolumeResult` that contains the details of the created volume.
        
        Raises:
            TypeError: If:
                * *size* is not a positive :obj:`int`
                * *snapshot_id* not a :obj:`str`
                * *volume_type* is not a :obj:`str`
                * *encrypted* is not of type :obj:`bool`
        """
        
        create_volume_request = CreateVolumeRequest()
        
        if size is not None:
            create_volume_request.size = size
            
        if snapshot_id is not None:
            create_volume_request.snapshot_id = snapshot_id
            
        if volume_type is not None:
            create_volume_request.volume_type = volume_type
            
        if encrypted is not None:
            create_volume_request.encrypted = encrypted
        
        
        query_params = {}
        query_params["Action"] = "CreateVolume"
        if create_volume_request.size != None:
            query_params["Size"] = create_volume_request.size
        
        if create_volume_request.snapshot_id != None:
            query_params["SnapshotId"] = create_volume_request.snapshot_id
        if create_volume_request.encrypted != None:
            query_params["Encrypted"] = create_volume_request.encrypted
        if create_volume_request.volume_type != None:
            query_params["VolumeType"] = create_volume_request.volume_type
        
        response = self.make_request(self._credentials, query_params, create_volume_request.custom_request_headers, "GET")
        
        response_data = str(response.read())
        try:
            if response.code // 100 == 2:
                volume_eo = objectify.fromstring(response_data)
                create_volume_result = CreateVolumeResult()
                create_volume_result.request_id = str(volume_eo.requestId)
                volume = Volume()
                volume.volume_id = str(volume_eo.volumeId)
                volume.status = str(volume_eo.status)
                volume.create_time = datetime.strptime(str(volume_eo.createTime), constants.RESPONSE_DATE_TIME_FORMAT)
                volume.size = int(volume_eo.size)
                volume.snapshot_id = str(volume_eo.snapshotId)
                volume.attachments = []
                volume.volume_type = str(volume_eo.volumeType)
                volume.encrypted = volume_eo.encrypted
                if hasattr(volume_eo.attachmentSet, "item"):
                    for attachment_eo in volume_eo.attachmentSet.item:
                        attachment = Attachment()
                        attachment.device = str(attachment_eo.device)
                        attachment.instance_id = str(attachment_eo.instanceId)
                        volume.attachments.append(attachment)
                create_volume_result.xml = response_data
                create_volume_result.volume = volume
                return create_volume_result
            else:
                raise HTTPException(response_data)
        finally:
            response.close()   

    
    def delete_volume(self, volume_id):
        """
        Deletes the snapshot with snapshot_id given in the argument.
        
        Args:
            snapshot_id (:obj:`str`): ID of the snapshot to delete.
                        
        Returns:
            An object of :class:`jcs_sbs_sdk.model.delete_snapshot_result.DeleteSnapshotResult` indicating if snapshot is deleted or not.
        
        Raises:
            TypeError: If *snapshot_id* is not of type :obj:`str`.
        """
        delete_volume_request = DeleteVolumeRequest()
        delete_volume_request.volume_id = volume_id
        
        query_params = {}
        query_params["Action"] = "DeleteVolume"
        query_params["VolumeId"] = utils.validate_string(delete_volume_request.volume_id, "volume_id")
        
        response = self.make_request(self._credentials, query_params, delete_volume_request.custom_request_headers, "GET")
        
        response_data = str(response.read())
        try:
            if response.code // 100 == 2:
                delete_volume_response = objectify.fromstring(response_data)
                delete_volume_result = DeleteVolumeResult()
                delete_volume_result.request_id = str(delete_volume_response.requestId)
                delete_volume_result.xml = response_data
                delete_volume_result.deleted = bool(getattr(delete_volume_response, "return"))
                return delete_volume_result
            else:
                raise HTTPException(response_data)
        finally:
            response.close()
        
        
    def describe_snapshots(self, snapshot_ids=None, next_token=None, max_results=None, detail=None):
        """
        Returns an object of the :class:`jcs_sbs_sdk.model.describe_snapshots_result.DescribeSnapshotsResult` containing the 
        :obj:`list` of :class:`jcs_sbs_sdk.model.snapshot.Snapshot` according to the corresponding internal API response.
        
        Args:
            snapshot_ids (:obj:`list` of :obj:`str`, optional, default = None): IDs of specific snapshot to be described.
            
            next_token (:obj:`str`, optional, default = None): ID of last snapshot in the previous call of the describe_snapshots() method.
                Previously, if the describe_snapshots() method is called with 'max_results' option, all items are not returned.
                To get the next set of snapshots, pass the ID of the last snapshot as 'next_token' in the subsequent call to the describe_snapshots() method.
                
            max_results (:obj:`int`, optional, default = None): Maximum number of snapshots to describe.
                To get the next set of snapshots, pass the ID of the last snapshot as 'next_token' in the subsequent call to the describe_snapshots() method.
            
            detail (:obj:`bool`, optional, default = None): Set *True* to describe the snapshots in detail.
        
        Returns:
            An object of the :class:`jcs_sbs_sdk.model.describe_snapshots_result.DescribeSnapshotsResult` containing the 
            :obj:`list` of :class:`jcs_sbs_sdk.model.snapshot.Snapshot` according to the corresponding internal API response.
        
        Raises:
            TypeError: If:
                * *snapshot_ids* is not a :obj:`list` of :obj:`str`
                * *next_token* is not of type :obj:`str`
                * *max_results* is not of type :obj:`int`
                * *detail* is not of type :obj:`bool`
        """
        
        describe_snapshots_request = DescribeSnapshotsRequest()
        
        if snapshot_ids is not None:
            describe_snapshots_request.snapshot_ids = snapshot_ids
            
        if next_token is not None:
            describe_snapshots_request.next_token = next_token
            
        if max_results is not None:
            describe_snapshots_request.max_results = max_results
            
        if detail is not None:
            describe_snapshots_request.detail = detail

        query_params = {}
        query_params["Action"] = "DescribeSnapshots"
        if describe_snapshots_request.max_results != None:
            query_params["MaxResults"] = describe_snapshots_request.max_results
        if describe_snapshots_request.next_token != None:
            query_params["NextToken"] = describe_snapshots_request.next_token
        if describe_snapshots_request.detail != None:
            query_params["Detail"] = describe_snapshots_request.detail
        if describe_snapshots_request.snapshot_ids != None:
            for i, snapshot_id in enumerate(describe_snapshots_request.snapshot_ids):
                query_params["SnapshotId.%d" % (i + 1)] = snapshot_id
        
        response = self.make_request(self._credentials, query_params, describe_snapshots_request.custom_request_headers, "GET")
        
        response_data = str(response.read())
        try:
            if response.code // 100 == 2:
                describe_snapshots_response = objectify.fromstring(response_data)
                describe_snapshots_result = DescribeSnapshotsResult()
                describe_snapshots_result.request_id = str(describe_snapshots_response.requestId)
                describe_snapshots_result.snapshots = []
                if hasattr(describe_snapshots_response.snapshotSet, "item"):
                    for snapshot_eo in describe_snapshots_response.snapshotSet.item:
                        snapshot = Snapshot()
                        snapshot.volume_id = str(snapshot_eo.volumeId)
                        snapshot.status = str(snapshot_eo.status)
                        if hasattr(snapshot_eo, "startTime"):
                            snapshot.start_time = datetime.strptime(str(snapshot_eo.startTime), constants.RESPONSE_DATE_TIME_FORMAT)
                        if hasattr(snapshot_eo, "volumeSize"):
                            snapshot.volume_size = int(snapshot_eo.volumeSize)
                        snapshot.snapshot_id = str(snapshot_eo.snapshotId)
                        if hasattr(snapshot_eo, "encrypted"):
                            snapshot.encrypted = snapshot_eo.encrypted
                        describe_snapshots_result.snapshots.append(snapshot)
                describe_snapshots_result.xml = response_data
                return describe_snapshots_result
            else:
                raise HTTPException(response_data)
        finally:
            response.close()

    def delete_snapshot(self, snapshot_id):
        """
        Deletes the snapshot with snapshot_id given in the DeleteSnapshotRequest object.
        
        Args:
            delete_snapshot_request (DeleteSnapshotRequest): An object of DeleteSnapshotRequest containing values required in create snapshot API.
            
        Returns:
            DeleteSnapshotResult object containing values in response given by the delete snapshot API.
        
        Raises:
            TypeError: If 'delete_snapshot_request' is not an instance of 'DeleteSnapshotRequest'.
        """
        delete_snapshot_request = DeleteSnapshotRequest()
        delete_snapshot_request.snapshot_id = snapshot_id
        
        query_params = {}
        query_params["Action"] = "DeleteSnapshot"
        query_params["SnapshotId"] = utils.validate_string(delete_snapshot_request.snapshot_id, "snapshot_id")
        
        response = self.make_request(self._credentials, query_params, delete_snapshot_request.custom_request_headers, "GET")
        
        response_data = str(response.read())
        try:
            if response.code // 100 == 2:
                delete_snapshot_response = objectify.fromstring(response_data)
                delete_snapshot_result = DeleteSnapshotResult()
                delete_snapshot_result.request_id = str(delete_snapshot_response.requestId)
                delete_snapshot_result.xml = response_data
                delete_snapshot_result.deleted = bool(getattr(delete_snapshot_response, "return"))
                return delete_snapshot_result
            else:
                raise HTTPException(response_data)
        finally:
            response.close()
        

    def create_snapshot(self, volume_id):
        """
        Creates a snapshot according to the arguments passed to this method and returns an object of :class:`jcs_sbs_sdk.model.create_snapshot_result.CreateSnapshotResult`.
        
        Args:
            volume_id (:obj:`str`): ID of volume from which the snapshot gets created.
          
        Returns:
            An object of :class:`jcs_sbs_sdk.model.create_snapshot_result.CreateSnapshotResult` that contains the details of the created snapshot.
        
        Raises:
            TypeError: If *volume_id* not of type :obj:`str`
        """
        
        create_snapshot_request = CreateSnapshotRequest()
        create_snapshot_request.volume_id = volume_id
        
        query_params = {}
        query_params["Action"] = "CreateSnapshot"
        query_params["VolumeId"] = utils.validate_string(create_snapshot_request.volume_id, "volume_id")
        
        response = self.make_request(self._credentials, query_params, create_snapshot_request.custom_request_headers, "GET")
        
        response_data = str(response.read())
        try:
            if response.code // 100 == 2:
                snapshot_eo = objectify.fromstring(response_data)
                create_snapshot_result = CreateSnapshotResult()
                create_snapshot_result.request_id = str(snapshot_eo.requestId)
                snapshot = Snapshot()
                snapshot.snapshot_id = str(snapshot_eo.snapshotId)
                snapshot.status = str(snapshot_eo.status)
                snapshot.start_time = datetime.strptime(str(snapshot_eo.startTime), constants.RESPONSE_DATE_TIME_FORMAT)
                snapshot.volume_size = int(snapshot_eo.volumeSize)
                snapshot.volume_id = str(snapshot_eo.volumeId)
                snapshot.encrypted = snapshot_eo.encrypted
                create_snapshot_result.xml = response_data
                create_snapshot_result.snapshot = snapshot
                return create_snapshot_result
            else:
                raise HTTPException(response_data)
        finally:
            response.close()   

