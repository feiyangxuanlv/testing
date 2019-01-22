import logging
from datetime import datetime
import threading
import readConfig
import os




class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        #print("resultPath:",resultPath)
        # 创建不存在的结果文件
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # 按本地时间定义测试结果文件名
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M")))
        #self.path = logPath
        #print("logPath:",logPath)
        # 创建不存在的日志文件
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.path = logPath
        # 定义日志记录器
        self.logger = logging.getLogger()
        # defined log level
        self.logger.setLevel(logging.INFO)

        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"),encoding='utf-8') #输出日志到文件


        # defined formatter

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        # add handler
        self.logger.addHandler(handler)



class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass


    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log


