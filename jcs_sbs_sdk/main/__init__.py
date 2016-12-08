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


jcs = JCSComputeClient()

def get_volume_status(volume_id):
    describe_volume_request = DescribeVolumesRequest()
    describe_volume_request.volume_ids=[volume_id]
    response = jcs.describe_volumes(describe_volume_request)
    print("Volume status: " + response.volumes[0].status)
    return response.volumes[0].status

def get_snapshot_status(snapshot_id):
    describe_snapshot_request = DescribeSnapshotsRequest()
    describe_snapshot_request.snapshot_ids=[snapshot_id]
    response = jcs.describe_snapshots(describe_snapshot_request)
    print("Snapshot status: " + response.snapshots[0].status)
    return response.snapshots[0].status

def print_json(inp_str):
    #print(inp_str)
    parsed = json.loads(str(inp_str))
    print json.dumps(parsed, indent=4)

def print_request_response(request,response):
    print("Request is:")
    print_json(request)
    print("Response is:")
    print_json(response)
 
print("*****************describe volumes*******************")
 
request = DescribeVolumesRequest()
request.detail = True
response = jcs.describe_volumes(request)
print(response.xml)
print_request_response(request, response)
 
print("*****************create volume*******************")
 
request = CreateVolumeRequest()
request.size = 10
response = jcs.create_volume(request)
volume_id = response.volume.volume_id
print(response.xml)
print_request_response(request, response)


print("*****************describe snapshots*******************")

request = DescribeSnapshotsRequest()
request.detail = True
print_json(request)
response = jcs.describe_snapshots(request)
print(response.xml)
print_request_response(request, response)

  
while get_volume_status(volume_id) != "available":
    sleep(60)
  
  
print("*****************create snapshot*******************")
  
request = CreateSnapshotRequest()
request.volume_id = volume_id
response = jcs.create_snapshot(request)
snapshot_id = response.snapshot.snapshot_id
print(response.xml)
print_request_response(request, response)
  
while get_snapshot_status(snapshot_id) != "completed":
    sleep(60)

print("*****************delete volume*******************")
  
request = DeleteVolumeRequest()
request.volume_id = volume_id
response = jcs.delete_volume(request)
print(response.xml)
print_request_response(request, response)
  
  
  
  
print("*****************delete snapshot*******************")
  
request = DeleteSnapshotRequest()
request.snapshot_id = snapshot_id
response = jcs.delete_snapshot(request)
print(response.xml)
print_request_response(request, response)


