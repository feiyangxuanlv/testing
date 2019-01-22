import unittest
import json

from time import sleep
from common.configDB import MyDB
from common import common
from common import configHttp
from common import configsign
from common.Log import MyLog
from common import configResults


class MyTestCase(unittest.TestCase):
    def setUp(self):  # 初始化环境
        print("Initialize the test environment")
        self.localReadConfig = MyDB() #定义链接数据库方法
        self.localReadConfig.connectDB()  #连接接数据库
        self.ExcelFile = common.get_xls("testcase.xls", "Sheet1") # 读取测试用例
        self.localconfigHttp = configHttp.ConfigHttp() # 定义请求方法
        self.localconfigsign = configsign.Configsign() # 定义签名方法
        self.logger = MyLog.get_log() # 定义日志方法
        self.Results = configResults.assertions() # 定义断言方法
        # 登陆请求
        self.localconfigHttp.set_url(self.ExcelFile[0][2])
        self.localconfigHttp.set_json(json.loads(self.ExcelFile[0][3]))
        self.localconfigHttp.set_headers(json.loads(self.ExcelFile[0][4]))
        self.login = self.localconfigHttp.post()
        self.token = self.login.cookies["CCWTOKEN"]
        self.Results.response_assertions(self.login,self.ExcelFile[0][5],self.ExcelFile[0][6],self.ExcelFile[0][0])

    def test_updateUser(self):
        self.localconfigHttp.set_url(self.ExcelFile[3][2])
        self.localconfigHttp.set_json(json.loads(self.ExcelFile[3][3]))
        self.localconfigHttp.set_headers(json.loads(self.ExcelFile[3][4]))
        self.localconfigHttp.set_cookie(self.login.cookies)
        self.localconfigsign.put_sign(self.localconfigHttp.headers,self.localconfigHttp.jsonl,self.token)
        self.updateUser = self.localconfigHttp.post()
        self.Results.response_assertions(self.updateUser,self.ExcelFile[3][5],self.ExcelFile[3][6],self.ExcelFile[3][0])

    def tearDown(self):    # 关闭测试环境
        self.localReadConfig.closeDB()
        print("Close the test environment")
        sleep(2)

if __name__ == '__main__':
    unittest.main()
