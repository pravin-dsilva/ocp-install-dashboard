import json

def job_details_pvm(user):
    list = []
    f = open('data.json',)
    data = json.load(f)
    i = data['builds']
    for j in i:
        k = j['actions']
        x = k[0]
        res = not bool(x)
        if res:
           continue
        if 'parameters' in x.keys():
           if len(x['parameters']) >= 11:
              z = x['parameters'][0]
              w = x['parameters'][1]
              y = x['parameters'][10]
              if y['name'] == 'UserName':
                 if y['value'] == user:
                    cn = z['value']
                    ov = w['value']
                    bn = j['number']
                    if j['result'] is None:
                       bs = 'Pending'
                    elif j['result'] == 'SUCCESS':
                       bs = 'Running'
                    elif j['result'] == 'FAILURE':
                       bs = 'Failed'
                    else:
                       continue
                    Dict = {}
                    Dict = dict({"ID":str(bn),"ClusterName":cn,"OcpVersion":ov,"Status":bs})
                    list.append(Dict)
    Dict = {}
    Dict = dict({'Cluster' : list})
    jd = json.dumps(Dict)
    print(jd)
    print('**********************************************')
    return jd
    f.close()

def job_details_pvs(user):
    list = []
    f = open('data.json',)
    data = json.load(f)
    i = data['builds']
    for j in i:
        k = j['actions']
        x = k[0]
        res = not bool(x)
        if res:
           continue
        if 'parameters' in x.keys():
           if len(x['parameters']) >= 10:
              z = x['parameters'][0]
              w = x['parameters'][1]
              y = x['parameters'][8]
              if y['name'] == 'UserName':
                 if y['value'] == user:
                    cn = z['value']
                    ov = w['value']
                    bn = j['number']
                    if j['result'] is None:
                       bs = 'Pending'
                    elif j['result'] == 'SUCCESS':
                       bs = 'Running'
                    elif j['result'] == 'FAILURE':
                       bs = 'Failed'
                    else:
                       continue
                    Dict = {}
                    Dict = dict({"ID":str(bn),"ClusterName":cn,"OcpVersion":ov,"Status":bs})
                    list.append(Dict)
    Dict = {}
    Dict = dict({'Cluster' : list})
    jd = json.dumps(Dict)
    print(jd)
    print('**********************************************')
    return jd
    f.close()
