# -*- coding: utf-8 -*-
import uiautomator2 as u2
from com.tomcatwang.common.adb_assign_device import adb_assign_device
import time
from com.tomcatwang.common.configParse import Config_Parse
device='d3cf3594'
configuration = Config_Parse(device)
d = u2.connect('d3cf3594')
adb = adb_assign_device('d3cf3594')
#adb.tap(47,92)
#d(resourceId='com.ss.android.ugc.aweme:id/kp').click()
return_page_menu=configuration.get_config_values('return_page_menu')
print(return_page_menu)
if return_page_menu != '' :
    print("=======================1")
    if(d(resourceId='com.ss.android.ugc.aweme:id/kp').exists(timeout=1)) :
        print("=======================2")
        d(resourceId='com.ss.android.ugc.aweme:id/kp').click()
    else :
        print("=======================3" + configuration.get_config_values("return_x") + "," + configuration.get_config_values("return_y"))
        adb.tap(int(configuration.get_config_values("return_x")),int(configuration.get_config_values("return_y")))
else :
    print("=======================4" + configuration.get_config_values("return_x") + "," + configuration.get_config_values("return_y"))
    adb.tap(int(configuration.get_config_values("return_x")),int(configuration.get_config_values("return_y")))
#xml = d.dump_hierarchy()
#print(xml)

#d(resourceId="com.ss.android.ugc.aweme:id/a53").click()
#xml = d.dump_hierarchy()
#print(xml)
adb.tap