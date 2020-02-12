# -*- coding: utf-8 -*-
import configparser
import re

def config_write():
    config = configparser.ConfigParser()
    self.config.read(self.configFilePath)