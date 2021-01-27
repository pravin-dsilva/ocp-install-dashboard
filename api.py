from flask import Flask, redirect, url_for, request, abort, render_template
import trigger
import destroy_alt
import json_collect
import json_process
import json
import os
import shutil
import time
import requests
app = Flask(__name__)
from flask_cors import CORS, cross_origin
cors = CORS(app)


@app.route('/test',methods = ['POST', 'GET'])
@cross_origin()
def test():
    if request.method == 'POST':
        print(request.headers)
        print(request.data)
        if not request.json:
            abort(400)
        print(request.json)
        return json.dumps(request.json)
    else:
        user = request.args.get('name')
        return 'hello %s' % user

@app.route('/hello/<name>')
@cross_origin()
def hello(name):
    return 'welcome %s' % name

@app.route('/',methods = ['POST', 'GET'])
@cross_origin()
def login():
    if request.method == 'POST':
        return redirect(url_for('hello',name = user))
    else:
        tenplates_loc = "templates"
        #shutil.rmtree(tenplates_loc, ignore_errors = True)
        #os.mkdir(tenplates_loc)
        #url = 'https://raw.githubusercontent.com/pravin-dsilva/ocp-install-dashboard/html-bootstrap/login.html'
        #r = requests.get(url, allow_redirects=True)
        #open(tenplates_loc + '/index.html', 'wb').write(r.content)
        message = "OpenShift on Power Deployment"
        return render_template('login.html', message=message)

@app.route('/create',methods = ['POST', 'GET'])
@cross_origin()
def landing():
    if request.method == 'POST':
        print(request.form)
        if not request.form:
            abort(400)
        data = request.form
        if "loginEmail" in data:
            login = data["loginEmail"]
        else:
            print('ERROR : Email address not provided')
        js_data=json.dumps(data)
        tenplates_loc = "templates"
        #shutil.rmtree(tenplates_loc, ignore_errors = True)
        #os.mkdir(tenplates_loc)
        #url = 'https://raw.githubusercontent.com/pravin-dsilva/ocp-install-dashboard/html-bootstrap/ocp-form.html'
        #r = requests.get(url, allow_redirects=True)
        #open(tenplates_loc + '/deploy.html', 'wb').write(r.content)
        message = "OpenShift on Power Deployment"
        return render_template('ocp-form.html',  js_data=js_data)


@app.route('/deploy',methods = ['POST', 'GET'])
@cross_origin()
def deploy():
    if request.method == 'POST':
        print(request.form)
        if not request.form:
            abort(400)
        data = request.form
        if "name" in data:
            email = data["emailid"]
            name = data["name"]
            description = data["description"]
            ocpversion = data["ocpversion"]
        else:
            print('ERROR : Cluster Name not provided')
        login_data=json.dumps(data)
        test_user = data["emailid"]
        platform = 'powervm'
        trigger.job_trigger(name,ocpversion,data["options"],test_user,platform)
        time.sleep(10)
        json_collect.job_data(platform)
        if platform == 'powervs':
           js_data = json_process.job_details_pvs(test_user)
        else:
           js_data = json_process.job_details_pvm(test_user)
        #write to db
        tenplates_loc = "templates"
        #url = 'https://raw.githubusercontent.com/pravin-dsilva/ocp-install-dashboard/html-bootstrap/displayStacks.html'
        #r = requests.get(url, allow_redirects=True)
        #open(tenplates_loc + '/displayStacks.html', 'wb').write(r.content)
        return render_template('displayStacks.html', js_data=js_data, login_data=login_data)

@app.route('/refresh',methods = ['POST', 'GET'])
@cross_origin()
def refreshStacks():
    print("refreshstackdata %s", request.form)
    if not request.form:
        abort(400)
    data = request.form
    test_user = data["emailid"]
    platform = 'powervm'
    json_collect.job_data(platform)
    login_data=json.dumps(data)
    if platform == 'powervs':
       js_data = json_process.job_details_pvs(test_user)
    else:
       js_data = json_process.job_details_pvm(test_user)
    tenplates_loc = "templates"
    #url = 'https://raw.githubusercontent.com/pravin-dsilva/ocp-install-dashboard/html-bootstrap/displayStacks.html'
    #r = requests.get(url, allow_redirects=True)
    #open(tenplates_loc + '/displayStacks.html', 'wb').write(r.content)
    return render_template('displayStacks.html', js_data=js_data, login_data=login_data)

@app.route('/delete',methods = ['POST', 'GET'])
@cross_origin()
def deleteCluster():
    data = request.form
    if "emailid" in data:
        login = data["emailid"]
    #Trigger delete cluster job
    test_user = data["emailid"]
    platform = 'powervm'
    destroy_alt.job_trigger(data['clusterid'],test_user,platform)
    time.sleep(10)
    json_collect.job_data(platform)
    login_data=json.dumps(data)
    if platform == 'powervs':
       js_data = json_process.job_details_pvs(test_user)
    else:
       js_data = json_process.job_details_pvm(test_user)
    return render_template('displayStacks.html', js_data=js_data, login_data=login_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True, threaded=True)
