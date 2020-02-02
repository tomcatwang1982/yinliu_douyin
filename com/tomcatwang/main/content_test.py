# -*- coding: utf-8 -*- 
import uiautomator2 as u2  
import time  
d=u2.connect('emulator-5554')  
d.app_start('com.ss.android.ugc.aweme')  
d(resourceId="com.ss.android.ugc.aweme:id/ys").click() 