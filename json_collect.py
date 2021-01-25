import requests
import json
from requests.auth import HTTPBasicAuth

def job_data():
    username = 'shilpi12@in.ibm.com'
    token = '<token>'

    get_url = 'http://molly.aus.stglabs.ibm.com:8090/job/demo-powervc-job-with-parameters/api/json'
    get_response = requests.get(get_url, params={"tree" : "builds[number,result,actions[parameters[name,value]]]"}, auth=HTTPBasicAuth(username, token)).json()

    with open('data.json', 'w') as outfile:
        json.dump(get_response, outfile)

def process_data(user):
    f = open('data.json',)
    data = json.load(f)
    for i in data['build']: 
        print('i')
    f.close()
