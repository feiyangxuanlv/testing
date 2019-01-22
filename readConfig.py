import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0] #获取当前文件路径，并去掉文件名字

configPath = os.path.join(proDir, "config.ini") #拼接config.ini文件路径

class ReadConfig:
    def __init__(self):
        fd = open(configPath,'r', encoding='gbk')
        data = fd.read()



        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

