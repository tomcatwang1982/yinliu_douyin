# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from com.tomcatwang.common.douyin_init import douyin_init
from com.tomcatwang.common.configParse import Config_Parse
from com.tomcatwang.common.log import Logger

#emulator-5554
#d3cf3594 oppo
#7460300e xiaomi
d = u2.connect('emulator-5554')
#d.app_start("com.github.uiautomator", "com.github.uiautomator.MainActivity")

#d(text="启动UIAUTOMATOR",resourceId="com.github.uiautomator:id/start_uiautomator").click()
d.app_stop("com.ss.android.ugc.aweme")
d.app_start("com.ss.android.ugc.aweme")

if (d(text="广州").exists(timeout=5)):
    d(text="广州").click()
elif (d(text="同城").exists(timeout=5)):
    d(text="同城").click()
time.sleep(3)

d(resourceId='com.ss.android.ugc.aweme:id/a53').click()


d(resourceId="com.ss.android.ugc.aweme:id/ys").click()
time.sleep(1)
for i in range(1,3):
    d(scrollable=True).scroll(steps=5)
    d(resourceId="com.ss.android.ugc.aweme:id/ir").click()
    time.sleep(2)
    d(resourceId="com.ss.android.ugc.aweme:id/ckn").click()
    time.sleep(2)
    d(text='私信').click()
    time.sleep(3)
    d(text="发送消息…").send_keys("hi,你好")
    time.sleep(3)
    d(resourceId='com.ss.android.ugc.aweme:id/d4i').click()
    time.sleep(2)
    d(description='返回').click()
    time.sleep(1)
    d(description='返回').click()
