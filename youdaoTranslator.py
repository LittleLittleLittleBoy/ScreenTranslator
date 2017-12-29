import json
import random
import time
import hashlib
import requests
def getText(text):
    salt=str(int(time.time()*1000) + random.randint(1,10))
    client='fanyideskweb'
    D= 'rY0D^0\'nM0}g5Mm1z%1G4'
    raw=client+text+salt+D
    md5=hashlib.md5()
    md5.update(raw.encode('utf-8'))
    sign=md5.hexdigest()
    data={
        'i': text,
        'from': 'en',
        'to': 'zh-CHS',
        'smartresult': "dict",
        'client': client,
        'salt': salt,
        'sign': sign,
        'doctype': "json",
        'version': "2.1",
        'keyfrom': "fanyi.web",
        'action':"FY_BY_DEFAULT",
        'typoResult': 'true'
    }
    kv = {"user-agent": "Mozilla/5.0"}
    r=requests.post('http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.google.com/',data,headers=kv)
    text = json.loads(str(r.text))
    return text.get('translateResult')[0][0]['tgt']


print(getText('hi'))
