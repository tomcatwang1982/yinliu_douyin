# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time

def douyin_init(d) :
    d.app_start("com.github.uiautomator", "com.github.uiautomator.MainActivity")
    d(text="启动UIAUTOMATOR",resourceId="com.github.uiautomator:id/start_uiautomator").click()

    d.app_stop("com.ss.android.ugc.aweme")
    d.app_start("com.ss.android.ugc.aweme")

    d(text="同城").wait(5)
    d(text="同城").click()
    time.sleep(3)
    d(resourceId="com.ss.android.ugc.aweme:id/aav").click()
    time.sleep(2)