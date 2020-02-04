# -*- coding: utf-8 -*-

import uiautomator2 as u2
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
        print(r,g,b,file=f)


