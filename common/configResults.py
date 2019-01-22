from common.Log import MyLog
import json
class assertions():


    def response_assertions(self,response,code,msg,casename):
        self.logger = MyLog.get_log()
        response = json.loads(response.text)
        try:
            if response["code"] == code and response["msg"] == msg :
                print("%s PASS " % casename)
                self.logger.logger.info(response)
            else:
                print("%s Fail " % casename)
                self.logger.logger.error(response)

        except:
            print("%s abnormal " % casename)
            self.logger.logger.error(response)

        #finally:
            #self.logger.logger.info(response)






