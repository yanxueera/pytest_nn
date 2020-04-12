import requests
from common.commonData import  CommonData
import json

class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}

    def post(self,path,data):
        proxies=CommonData.proxies
        host=CommonData.host
        data_json=json.dumps(data)
        self.headers['token']=CommonData.token
        resp=self.http.post(url=host+path,
                            proxies=proxies,
                            data=data_json,
                            headers=self.headers)
        assert resp.status_code==200
        resp_json=resp.text
        resp_dict=json.loads(resp_json)
        return resp_dict
