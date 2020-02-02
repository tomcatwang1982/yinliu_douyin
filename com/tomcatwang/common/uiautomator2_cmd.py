# -*- coding: utf-8 -*-
import uiautomator2 as u2
import time

class Uiautomator2Cmd(object) :
    __conn = None

    def __init__(self, connect_string):
        self.__conn = u2.connect(connect_string)

    def app_start(self,
                  package_name,
                  activity=None,
                  extras={},
                  wait=False,
                  stop=False,
                  unlock=False,
                  launch_timeout=None,
                  use_monkey=False):
        self.__conn.app_start(package_name,activity,extras,wait,stop,unlock,launch_timeout,use_monkey)

    def app_current(self):
        self.__conn.app_current()

    def app_stop(self, pkg_name):
        self.__conn.app_stop(pkg_name)

    def d_click(self,**kwargs):
        #print(kwargs)
        self.__conn(**kwargs).click()

    def __del__(self):
        pass

cls = Uiautomator2Cmd('emulator-5554')
#cls.app_stop('com.ss.android.ugc.aweme')
#cls.app_start('com.ss.android.ugc.aweme')
a="com.ss.android.ugc.aweme:id/ys"
cls.d_click(resourceId=a)
