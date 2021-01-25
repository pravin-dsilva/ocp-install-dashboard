import requests
from requests.auth import HTTPBasicAuth

def job_trigger(bn,user,platform):
    username = 'shilpi12@in.ibm.com'
    token = '<token>'

    if platform == 'powervs':
       job = 'demo-powervs-job-with-parameters'
    else:
       job = 'demo-powervc-job-with-parameters'

    post_url = 'http://molly.aus.stglabs.ibm.com:8090/job/{}/{}/doDelete'.format(job,bn)
    post_response = requests.post(post_url, auth=HTTPBasicAuth(username, token))
    print(post_response.status_code)

