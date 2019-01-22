import requests
import readConfig as readConfig
from common.Log import MyLog


#import hashlib
#import json
localReadConfig = readConfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.logger = MyLog.get_log()
        #self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.jsonl = {}
        self.cookie = None

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header,):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    def set_json(self, jsonl):
        self.jsonl = jsonl  # encode(encoding='UTF-8')

    def set_cookie(self,cookie):
        self.cookie = cookie
    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, json=self.jsonl,cookies= self.cookie, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            #print("Time out!")
            self.logger.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:

            response = requests.post(self.url, headers=self.headers, data=self.data, json=self.jsonl, cookies= self.cookie, files=self.files,timeout=float(timeout))
            # response.raise_for_status()
            return response


        except TimeoutError:
            #print("Time out!")
            self.logger.logger.error("Time out!")
            return None