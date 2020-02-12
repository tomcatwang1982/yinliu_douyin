# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from com.tomcatwang.common.log import Logger

def douyin_init(d) :
    d.app_start("com.github.uiautomator", "com.github.uiautomator.MainActivity")
    d(text="启动UIAUTOMATOR",resourceId="com.github.uiautomator:id/start_uiautomator").click()

    d.app_stop("com.ss.android.ugc.aweme")
    d.app_start("com.ss.android.ugc.aweme")

    d(text="广州").wait(5)
    d(text="广州").click()
    time.sleep(3)
    #xml = d.dump_hierarchy()
    #print(xml)
    d(resourceId="com.ss.android.ugc.aweme:id/aay").click()
    time.sleep(2)
    print("程序初始化完成....................................................................")