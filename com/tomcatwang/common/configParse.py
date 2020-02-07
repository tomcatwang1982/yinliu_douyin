# -*- coding:utf-8 -*-
import os
import configparser


class Config_Parse:

    def __init__(self, config_type):
        self.config_type = config_type

        # 项目路径
        rootDir = os.path.split(os.path.realpath(__file__))[0]

        # config.ini文件路径
        configFilePath = os.path.join(str(rootDir) + "/config", self.config_type)

    def get_config_values(self, section, option):
        """
         根据传入的section获取对应的value
         :param section: ini配置文件中用[]标识的内容
         :return:
         """
        config = configparser.ConfigParser()
        config.read(self.configFilePath)
        # return config.items(section=section)
        return config.get(section=section, option=option)
