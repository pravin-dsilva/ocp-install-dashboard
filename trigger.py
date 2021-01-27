import requests
from requests.auth import HTTPBasicAuth

def job_trigger(name,ocpversion,flavor,user,platform):
    username = 'shilpi12@in.ibm.com'
    token = '<token>'

    if platform == 'powervs':
       job = 'demo-powervs-job-with-parameters'
       if flavor == 'small':
          req_obj = {'json' : '{"parameter":[{"name":"ClusterName","value":"'+name+'"},{"name":"OcpRelease","value":"'+ocpversion+'"},{"name":"MemMaster","value":"16"},{"name":"ProcessorMaster","value":".5"},{"name":"CountMaster","value":"3"},{"name":"MemWorker","value":"16"},{"name":"ProcessorWorker","value":".5"},{"name":"CountWorker","value":"2"},{"name":"UserName","value":"'+user+'"},{"name":"Region","value":"lon"}]}', 'token' : ''+token}
       elif flavor == 'medium':
          req_obj = {'json' : '{"parameter":[{"name":"ClusterName","value":"'+name+'"},{"name":"OcpRelease","value":"'+ocpversion+'"},{"name":"MemMaster","value":"32"},{"name":"ProcessorMaster","value":"1"},{"name":"CountMaster","value":"3"},{"name":"MemWorker","value":"32"},{"name":"ProcessorWorker","value":"1"},{"name":"CountWorker","value":"2"},{"name":"UserName","value":"'+user+'"},{"name":"Region","value":"lon"}]}', 'token' : ''+token}
       else:
          req_obj = {'json' : '{"parameter":[{"name":"ClusterName","value":"'+name+'"},{"name":"OcpRelease","value":"'+ocpversion+'"},{"name":"MemMaster","value":"32"},{"name":"ProcessorMaster","value":"1"},{"name":"CountMaster","value":"3"},{"name":"MemWorker","value":"64"},{"name":"ProcessorWorker","value":"1"},{"name":"CountWorker","value":"3"},{"name":"UserName","value":"'+user+'"},{"name":"Region","value":"lon"}]}', 'token' : ''+token}
    else:
       job = 'demo-powervc-job-with-parameters'
       if flavor == 'small':
          req_obj = {'json' : '{"parameter":[{"name":"ClusterName","value":"'+name+'"},{"name":"OcpRelease","value":"'+ocpversion+'"},{"name":"VcpusMaster","value":"1"},{"name":"MemMaster","value":"16"},{"name":"ProcessorMaster","value":".5"},{"name":"CountMaster","value":"3"},{"name":"VcpusWorker","value":"1"},{"name":"MemWorker","value":"16"},{"name":"ProcessorWorker","value":".5"},{"name":"CountWorker","value":"2"},{"name":"UserName","value":"'+user+'"}]}', 'token' : ''+token}
       elif flavor == 'medium':
          req_obj = {'json' : '{"parameter":[{"name":"ClusterName","value":"'+name+'"},{"name":"OcpRelease","value":"'+ocpversion+'"},{"name":"VcpusMaster","value":"1"},{"name":"MemMaster","value":"32"},{"name":"ProcessorMaster","value":"1"},{"name":"CountMaster","value":"3"},{"name":"VcpusWorker","value":"1"},{"name":"MemWorker","value":"32"},{"name":"ProcessorWorker","value":"1"},{"name":"CountWorker","value":"2"},{"name":"UserName","value":"'+user+'"}]}', 'token' : ''+token}
       else:
          req_obj = {'json' : '{"parameter":[{"name":"ClusterName","value":"'+name+'"},{"name":"OcpRelease","value":"'+ocpversion+'"},{"name":"VcpusMaster","value":"1"},{"name":"MemMaster","value":"32"},{"name":"ProcessorMaster","value":"1"},{"name":"CountMaster","value":"3"},{"name":"VcpusWorker","value":"1"},{"name":"MemWorker","value":"64"},{"name":"ProcessorWorker","value":"1"},{"name":"CountWorker","value":"3"},{"name":"UserName","value":"'+user+'"}]}', 'token' : ''+token}

    post_url = 'http://molly.aus.stglabs.ibm.com:8090/job/{}/build'.format(job)
    post_response = requests.post(post_url, data=req_obj, auth=HTTPBasicAuth(username, token))
    print(post_response.status_code)

