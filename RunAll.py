import unittest
import MyHTMLTestRunner
import readConfig
import os
#from common.Log import *
from common.configEmail import MyEmail
from common.Log import MyLog
#from common.Log import Log
#from common.Log import Log as getlogpath
#from datetime import datetime
#logger = MyLog().get_log()
#reprotPath = os.path.join(os.path.join(os.path.join(readConfig.proDir, "result"), str(datetime.now().strftime("%Y%m%d%H%M"))),"report.html")


class Runall:

    def set_case_list(self):
        self.casepath = os.path.join(readConfig.proDir,"caselist.txt")
        self.caseList =[]
        fb = open(self.casepath,"r",encoding="UTF-8")
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.caseList:
            case_file = os.path.join(readConfig.proDir, "testCase")
            #print(case_file)
            case_name = case.split("/")[-1]
            #print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
            suite_model.append(discover)

        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            self.logger = MyLog.get_log()
            reprotPath = os.path.join(readConfig.proDir,"result",os.listdir(os.path.join(readConfig.proDir,"result"))[-1],"report.html")
            print(reprotPath)
            #self.reprotPath = os.path.join(os.path.join(os.path.join(readConfig.proDir, "result"), str(datetime.now().strftime("%Y%m%d%H%M"))),"report.html")
            #self.reprotPath = os.path.join(str(MyLog.get_path()), "report.html")
            if suit is not None:
                self.logger.logger.info("********TEST START********")
                fp = open(reprotPath, 'wb')
                runner = MyHTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='登陆接口测试')
                runner.run(suit)
            else:
                self.logger.logger.info("Have no case to test.")
        except Exception as ex:
            self.logger.logger.error(str(ex))
        finally:
            self.logger.logger.info("*********TEST END*********")
            localReadConfig = readConfig.ReadConfig()
            self.email = MyEmail().get_email()
            # send test report by email
            if int(localReadConfig.get_email("on_off")) == 0:
                #pass
                self.email.send_email()
            elif int(localReadConfig.get_email("on_off")) == 1:
                self.logger.logger.info("Doesn't send report email to developer.")
            else:
                self.logger.logger.info(" Unknow state.")



Runall().run()