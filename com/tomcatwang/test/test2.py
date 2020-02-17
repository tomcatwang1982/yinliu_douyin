# -*- coding: utf-8 -*-
import uiautomator2 as u2
import random,time
from com.tomcatwang.common.adb_assign_device import adb_assign_device

device='emulator-5554'
d = u2.connect(device)

#xml = d.dump_hierarchy()
#print(xml)

page_down_x1=330
page_down_y1=782
page_down_x2=341
page_down_y2=99
d.swipe(page_down_x1, page_down_y1, page_down_x2, page_down_y2)

#d(resourceId='com.ss.android.ugc.aweme:id/dc0').click()
#d.drag(page_down_x1, page_down_y1, page_down_x2, page_down_y2)