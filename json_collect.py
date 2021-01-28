import requests
import json
from requests.auth import HTTPBasicAuth

def job_data(platform):
    username = 'shilpi12@in.ibm.com'
    token = '<token>'

    if platform == 'PowerVS':
       job = 'demo-powervs-job-with-parameters'
    else:
       job = 'demo-powervc-job-with-parameters'

    get_url = 'http://molly.aus.stglabs.ibm.com:8090/job/{}/api/json'.format(job)
    get_response = requests.get(get_url, params={"tree" : "builds[number,result,actions[parameters[name,value]]]"}, auth=HTTPBasicAuth(username, token)).json()

    with open('data.json', 'w') as outfile:
        json.dump(get_response, outfile)

def process_data(user):
    f = open('data.json',)
    data = json.load(f)
    for i in data['build']: 
        print('i')
    f.close()
