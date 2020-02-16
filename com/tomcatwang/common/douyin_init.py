# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from com.tomcatwang.common.log import Logger
from com.tomcatwang.common.configParse import Config_Parse

def douyin_init(d,device,config_path) :
    configuration = Config_Parse(device,config_path)
    d.app_start("com.github.uiautomator", "com.github.uiautomator.MainActivity")

    #xml = d.dump_hierarchy()
    #print(xml)

    d(text="启动UIAUTOMATOR",resourceId="com.github.uiautomator:id/start_uiautomator").click()
    #com.github.uiautomator:id/start_uiautomator

    d.app_stop("com.ss.android.ugc.aweme")
    d.app_start("com.ss.android.ugc.aweme")

    d(text="广州").wait(5)
    d(text="广州").click()
    time.sleep(3)
    #xml = d.dump_hierarchy()
    #print(xml)
    #点击同城第一个视频
    #d(resourceId="com.ss.android.ugc.aweme:id/aay").click()
    city_menu=configuration.get_config_values('city_menu')
    print('city_menu---------------------> is : ' + str(city_menu))
    d(resourceId=city_menu).click()
    time.sleep(2)
    print("程序初始化完成....................................................................")
#d = u2.connect('2529b8a80906')
#douyin_init(d)