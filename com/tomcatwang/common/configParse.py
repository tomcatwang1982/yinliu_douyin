# -*- coding:utf-8 -*-
import os
import configparser


class Config_Parse:
    configFilePath = ""
    config_type = ""
    device = ""
    config = None
    def __init__(self, device, config_type=None):
        self.config_type = config_type
        self.device = device
        # 项目路径
        #rootDir = os.path.split(os.path.realpath(__file__))[0]

        # config.ini文件路径
        rootDir = os.path.abspath(os.path.dirname(__file__)).split('yinliu_douyin')[0] + "yinliu_douyin"
        self.configFilePath = rootDir + "\config" +  "\\" + self.device + ".ini"
        #print(self.configFilePath)
        self.config = configparser.ConfigParser()
        #print(self.configFilePath)
        self.config.read(self.configFilePath)


    def get_config_values(self, option, section='tomcatwang'):
        """
         根据传入的section获取对应的value
         :param section: ini配置文件中用[]标识的内容
         :return:
         """


        # return config.items(section=section)
        return self.config.get(section=section, option=option)

if __name__ == '__main__':
    configuration = Config_Parse("7460300e")
    #print(configuration.get_config_values('ServerAliveInterval','tomcatwang'))
    print(configuration.get_config_values("page_down_x1",'tomcatwang'))
