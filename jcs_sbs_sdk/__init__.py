__version__ = '1.0.0'


import json
from time import sleep

from jcs_sbs_sdk.auth.credentials import Credentials
from jcs_sbs_sdk.model.create_snapshot_request import CreateSnapshotRequest
from jcs_sbs_sdk.model.create_volume_request import CreateVolumeRequest
from jcs_sbs_sdk.model.delete_snapshot_request import DeleteSnapshotRequest
from jcs_sbs_sdk.model.delete_volume_request import DeleteVolumeRequest
from jcs_sbs_sdk.model.describe_snapshots_request import DescribeSnapshotsRequest
from jcs_sbs_sdk.model.describe_volumes_request import DescribeVolumesRequest
from jcs_sbs_sdk.service.jcs_compute_client import JCSComputeClient



def INFO():
    """
    This is the parent module of all the modules in this SDK.
    The __init__ file of this module shows how to create/describe/delete the volumes and snapshots with basic examples.
    Following utility methods are used in the example code only in this file.
    """
    pass

def get_volume_status(volume_id):
    """
    Returns the status of the volume with given volume ID.
    
    Args:
        volume_id (str): ID of the volume.
    
    Returns:
        Volume's current status (str).
    """
    response = jcs.describe_volumes(volume_ids=[volume_id])
    print("Volume status: " + response.volumes[0].status)
    return response.volumes[0].status

def get_snapshot_status(snapshot_id):
    """
    Returns the status of the snapshot with given snapshot ID.
    
    Args:
        snapshot_id (str): ID of the snapshot.
    
    Returns:
        Snapshot's current status (str).
    """
    response = jcs.describe_snapshots(snapshot_ids=[snapshot_id])
    print("Snapshot status: " + response.snapshots[0].status)
    return response.snapshots[0].status

def print_json(inp_str):
    """
    Prints the given JSON string after adding indentation to make it more readable.
    
    Args:
        inp_str (str): The JSON string which is to be pretty printed.
    """
    #print(inp_str)
    if(inp_str is None):
        return
    parsed = json.loads(str(inp_str))
    print json.dumps(parsed, indent=4)

def print_request_response(request,response):
    """
    Pretty prints request and response objects in json format. Additionally it also prints the backend API's XML response.
    It also labels them to make the output more readable. 
    
    Args:
        request (instance of JCSRequest class): The request object used to call the SBS service method.
        
        response (instance of JCSResult class): The response object returned by the SBS service method.
    """
    print("\nRequest object in JSON is:")
    print_json(request)
    print("\nAPI response XML is:")
    print(response.xml)
    print("\nSDK Response object in JSON is:")
    print_json(response)

jcs = JCSComputeClient()
 
print("\n*****************describe volumes*******************")
   
response = jcs.describe_volumes()
print_request_response(None, response)
 
print("\n*****************create volume*******************")
   
request = CreateVolumeRequest()
request.size = 10
response = jcs.create_volume(size=10)
volume_id = response.volume.volume_id
print_request_response(request, response)
 
 
print("\n*****************describe snapshots*******************")
 
request = DescribeSnapshotsRequest()
request.detail = True
response = jcs.describe_snapshots(detail=True)
print_request_response(request, response)
 
    
while get_volume_status(volume_id) != "available":
    sleep(60)
    
    
print("\n*****************create snapshot*******************")
    
request = CreateSnapshotRequest()
request.volume_id = volume_id
response = jcs.create_snapshot(volume_id=volume_id)
snapshot_id = response.snapshot.snapshot_id
print_request_response(request, response)
 
 
snapshot_status = get_snapshot_status(snapshot_id)
while snapshot_status != "completed" and snapshot_status != "error":
    sleep(60)
    snapshot_status = get_snapshot_status(snapshot_id)
  
print("\n*****************delete volume*******************")
 
request = DeleteVolumeRequest()
request.volume_id = volume_id
response = jcs.delete_volume(volume_id=volume_id)
print_request_response(request, response)
    
    
    
    
print("*****************delete snapshot*******************")
    
request = DeleteSnapshotRequest()
request.snapshot_id = snapshot_id
response = jcs.delete_snapshot(snapshot_id=snapshot_id)
print_request_response(request, response)
