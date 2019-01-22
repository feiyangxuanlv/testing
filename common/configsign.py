import hashlib

from common import configHttp

localconfigHttp = configHttp.ConfigHttp()

class Configsign:
    def put_sign(self,header,date,token):
        #print("签名前:",header)
        #print("请求体：",date)
        signdate = str(date) + token
        signdate = signdate.replace("\'", "\"")
        #print("加密体转义之后：",signdate)
        sign = hashlib.md5(signdate.encode(encoding='UTF-8')).hexdigest()
        signs = {"sign":sign}
        self.headers = header.update(signs)
    #def put_url(self,url,variable,location):
        #dict = str(url).split("/")

