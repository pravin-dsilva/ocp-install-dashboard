import requests
from requests.auth import HTTPBasicAuth

def job_trigger(bn,user):
    username = 'shilpi12@in.ibm.com'
    token = '<token>'

    post_url = 'http://molly.aus.stglabs.ibm.com:8090/job/demo-powervc-job-with-parameters/{}/doDelete'.format(bn)
    post_response = requests.post(post_url, auth=HTTPBasicAuth(username, token))
    print(post_response.status_code)

