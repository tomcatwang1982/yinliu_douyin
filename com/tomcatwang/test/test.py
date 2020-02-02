# -*- coding: utf-8 -*-
import uiautomator2 as u2
import time

d = u2.connect('emulator-5554') # connect to device
#d.screen_on()
#emulator-5554
#d3cf3594 oppo
#7460300e xiaomi
#print(d.info)

d.app_start("com.tencent.mobileqq")
#xml = d.dump_hierarchy()
#print(xml)
#print(d(text='动态').info)
#d(text='动态').click(917,2101)
time.sleep(2)
d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout[3]').click()#动态
#d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout[2]').click()#看点
#d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[1]').click()#消息
#d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout[1]').click()#联系人
#d.xpath('//*[@resource-id="com.tencent.mobileqq:id/input"]/android.widget.EditText[0]').click()
#tap(900,2000)
time.sleep(2)
#d.wait_activity('com.tencent.mobileqq.activity.SplashActivity', timeout=10)
#tap(947,2247)
#print("---------------2")
d(text="扩列").click()
time.sleep(2)
d(text="限时聊天，点击匹配").click()
time.sleep(2)
#d(text="匹配").click()
#time.sleep(2)
d(text="开始匹配").click()
#xml = d.dump_hierarchy()
#print(xml)
time.sleep(2)
#tap(531,1183)
#tap(0,2088)
#tap(42,2122)
#input_text("xxxxxxxxxxxxxx")
#time.sleep(2)
#tap(991,1576)
#d(resourceId="com.tencent.mobileqq:id/input").send_keys("ceshi06")
#d(resourceId="com.tencent.mobileqq:id/inputBar").swipe("")
#d.xpath('//*[@resource-id="com.tencent.mobileqq:id/input"]/android.widget.EditText[0]').click()
#time.sleep(2)
#tap(1010,2183)
