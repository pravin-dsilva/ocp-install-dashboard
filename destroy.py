import requests
from requests.auth import HTTPBasicAuth

def job_trigger(bn,user):
    username = 'shilpi12@in.ibm.com'
    token = '<token>'

    req_obj = {'json' : '{"parameter":[{"name":"JobNo","value":"'+bn+'"},{"name":"UserName","value":"'+user+'"}]}', 'token' : ''+token}

    post_url = 'http://molly.aus.stglabs.ibm.com:8090/job/demo-powervs-destroy-job/build'
    post_response = requests.post(post_url, data=req_obj, auth=HTTPBasicAuth(username, token))
    print(post_response.status_code)

