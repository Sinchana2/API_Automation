import requests
import json
import pytest
from Utilities.customLogger import LogGen
class api_test():

    _log= LogGen()

    def get_token(self,url):
        data ={ 'username': 'admin', 'password': 'password123'}
        r = requests.post(url, data =json.dumps(data), verify=False)
        token = json.loads(r.text)['session']
        return token

    def set_headers(self):
        #token = self.get_token(url)
        headers = {'Content-Type': 'application/json','Accept': 'application/json'}
        return headers

    def get_resources(self, url):

        _resPass = '200'
        _resFail = ['[404]','[401]','[403]','[500]']
        # token = self.get_token(url)
        resStatus = requests.get(url)

        restext = resStatus.json()
        if _resPass in str(resStatus.status_code):
            print('Response code is {}. Get method successfully executed'.format(_resPass))
            print('Json response is "{}"'.format(restext))
            assert str(resStatus.status_code)== _resPass

        else:
            print('Response code is "{}". Get method failed on execution'.format(_resFail))
            self._log.loggen()

    def create_resources(self,url,kwargs):
        _resPass = '200'
        _resFail ="['[400]','[401]','[404]','[403]']"
        _resCreate = '201'
        for arg in kwargs:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            respStatus = requests.post(url,headers= headers,data=json.dumps(arg), verify=False)

            assert respStatus.status_code == 200

            restext = requests.Response.json(respStatus)

            if _resPass in str(respStatus.status_code):
                print('Response code is {}. Post method successfully executed'.format(_resPass))
                print('Json response is "{}"'.format(restext))
                self._log.loggen()

            else:
                print('Response code is "{}". Post method failed on execution'.format(_resFail))

    def create_resource(self,url,data):
        _resPass = '200'
        _resFail =['[400]','[401]','[404]','[403]']
        _resCreate = '201'

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        respStatus = requests.post(url, headers=headers,data=json.dumps(data), verify=False)

        print(respStatus.status_code)
        assert respStatus.status_code == 200

        restext = requests.Response.json(respStatus)

        if _resPass in str(respStatus.status_code):
            print('Response code is {}. Post method successfully executed'.format(_resPass))
            print('Json response is "{}"'.format(restext))
            self._log.loggen()
        else:
            print('Response code is "{}". Post method failed on execution'.format(_resFail))

    def update_resource(self, url, data):
        _resPass = '200'
        _resFail = ['[400]','[401]','[403]','[404]','[500]','[501]']

        resStatus1 = requests.get(url)
        restext=resStatus1.json()
        print("resources before updation is {}".format(restext))

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        resStatus2 = requests.put(url,headers=headers,data=json.dumps(data),verify=False)
        resText = requests.Response.json(resStatus2)

        assert str(resStatus2.status_code) == _resPass

        if str(resStatus2.status_code) == '200':
            print("Response code is {}. Put method successfully executed".format(_resPass))
            print("Json response is {}. Data has been successfully updated".format(resText))
        else:
            print("Response code is {}. Updating the data failed".format(_resFail))

    def delete_resource(self, url):
        _resPass = '200'
        _resFail = ['[400]','[401]','[403]','[404]','[500]','[501]']

        resStatus = requests.delete(url)
        resText = resStatus.json()
        assert str(resStatus.status_code) == _resPass
        if str(resStatus.status_code) == _resPass:
            print("Status code is {}. Resource has been deleted".format(resStatus.status_code))
            print("Deleted resource details are {}.".format(resText))
        else:
            print("Status code is {}. Resource could not be deleted.".format(_resFail))
