# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from com.tomcatwang.common.adb import swipe, tap

d = u2.connect('7460300e')
d.click(61,143)
'''
d.app_start("com.github.uiautomator", "com.github.uiautomator.MainActivity")
d(text="启动UIAUTOMATOR",resourceId="com.github.uiautomator:id/start_uiautomator").click()


d.app_start("com.ss.android.ugc.aweme")

#d(text="同城").wait(5)
#d(text="同城").click()
#time.sleep(3)
#d(resourceId="com.ss.android.ugc.aweme:id/aav").click()
#time.sleep(1)
d(resourceId='com.ss.android.ugc.aweme:id/zc').click()
time.sleep(1)

#for i in range(0, 19):

if d(resourceId="com.ss.android.ugc.aweme:id/a81", index=str(0)).exists(timeout=3):
    d(resourceId="com.ss.android.ugc.aweme:id/a81", index=str(0)).child(
        resourceId="com.ss.android.ugc.aweme:id/bzo").child(
        resourceId="com.ss.android.ugc.aweme:id/jo").click()
time.sleep(2)
tap(61, 143)
time.sleep(2)

if d(resourceId="com.ss.android.ugc.aweme:id/bzo", index="1").exists(timeout=3):
    print("-----------------------------1")
    d(resourceId="com.ss.android.ugc.aweme:id/bzo", index="1").child(
        resourceId="com.ss.android.ugc.aweme:id/a81").child(
        resourceId="com.ss.android.ugc.aweme:id/jo").click()
time.sleep(2)
tap(61, 143)
#xml = d.dump_hierarchy()
#print(xml)


from PIL import Image

#d = u2.connect('emulator-5554')
#d.app_start("com.ss.android.ugc.aweme")
#d(resourceId="com.ss.android.ugc.aweme:id/ys").click()
f = open("C:\\Users\\tomcatwang\\Desktop\\yinliu\\o.txt","w+")
im = Image.open("C:\\Users\\tomcatwang\\Desktop\\yinliu\\xxx.JPG")
rgb_im = im.convert('RGB')
for i in range(256) :
    for j in range(256) :
        r,g,b = rgb_im.getpixel((i,j))
        print(r,g,b,file=f)W
'''
