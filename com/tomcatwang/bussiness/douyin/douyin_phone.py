# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time,re
from com.tomcatwang.common.adb import swipe,tap
from goto import with_goto

#xml = d.dump_hierarchy()
#print(xml)
#emulator-5554
#d3cf3594 oppo
#7460300e xiaomi
##connect device
#'192.168.3.12:5555'
d = u2.connect('192.168.3.8:5555')
#com.ss.android.ugc.aweme.main.MainActivity
##start atx
#d.app_start("com.github.uiautomator","com.github.uiautomator.MainActivity")
#d(resourceId="com.github.uiautomator:id/start_uiautomator").click()
#xml = d.dump_hierarchy()
#print(xml)
time.sleep(2)
d.press("home")
##start app
d.app_start("com.ss.android.ugc.aweme")

#loop video num 需要循环观看多少个视频
loop_video_num = 30

for j in range(1,loop_video_num):
    #loop message num 需要循环多少个留言用户
    loop_message_num = 6
    #pagedown
    swipe(501,1819,497,265)
    #loop wait message button appear

    if d.exists(resourceId='com.ss.android.ugc.aweme:id/zc') :
        d(resourceId='com.ss.android.ugc.aweme:id/zc').click()

    ##message total num

    ##get ping lun shu
    try :
        message_total = str((d(resourceId='com.ss.android.ugc.aweme:id/a50').info['contentDescription']))
        str_ping_lun_total = re.findall("([1-9]+)",message_total)[0]
        print("str_ping_lun_total=" + str_ping_lun_total)
        if (str_ping_lun_total != '' and str_ping_lun_total.rfind('w') > 0) :
            #print("=================111")
            str_ping_lun_total = str_ping_lun_total.replace(str_ping_lun_total,'w','0000')
            int_ping_lun_total = int(float(str_ping_lun_total) * 10000)
        else :
            #print("=================222")
            int_ping_lun_total = int(str_ping_lun_total)
    except Exception as e:
        print(e)
        print("=================333")
        int_ping_lun_total = 0
        #xml = d.dump_hierarchy()
        #print(xml)
        tap(194,424)
        d(resourceId='com.ss.android.ugc.aweme:id/aze').click() #同城中可以，推荐中不行

    print(int_ping_lun_total)
    ###message num if > 0
    if (int_ping_lun_total > 0) :
        print('---------------------j='+str(j))
        if (int_ping_lun_total <= loop_message_num) :
            #if message num < 设定的评论数
            loop_message_num = int_ping_lun_total
        #print('---------------------2')
        for i in range(1,loop_message_num) :
            try :
                print('---------------------i='+str(i))
                #if_continue = False
                if d(resourceId="com.ss.android.ugc.aweme:id/a81",index=str(i)).exists(timeout=3) :
                    d(resourceId="com.ss.android.ugc.aweme:id/a81",index=str(i)).child(resourceId="com.ss.android.ugc.aweme:id/bzo").child(resourceId="com.ss.android.ugc.aweme:id/jo").click()

                    if (d(text="取消关注").exists() or d(text="相互关注").exists()):
                        print("----取消关注----")
                        d(description='返回').click()
                    '''
                    print('---------------------4')
                    if d.exists(text="取消关注") :
                        if_continue = True
                        d(description='返回').click()
                        break
                    print('---------------------5')
                    if (if_continue) :
                        continue
                    '''
                    #xml = d.dump_hierarchy()
                    #print(xml)
                    if d(resourceId='com.ss.android.ugc.aweme:id/axp').exists(timeout=3) :
                        if d(description='返回').exists(timeout=1) :
                            d(description='返回').click()
                        time.sleep(2)
                        continue

                    if d(text="关注").exists(timeout=1) :
                        d(text="关注").click()
                        time.sleep(1)


                    if d(text="私信").exists(timeout=1) :
                        d(text='私信').click()
                        time.sleep(1)
                    else :#如果没有私信就返回
                        print("-------------------------------------1")
                        d(description='返回').click()

                    if d(text="发送消息…").exists(timeout=1) :
                        d(text="发送消息…").send_keys("hi,你好")
                        time.sleep(3)

                    #xml = d.dump_hierarchy()
                    #print(xml)
                    if d(description="发送").exists(timeout=1) :
                        d(description="发送").click()
                        time.sleep(5)


                    '''
                    #发送消息
                    while(True):
                        if d.exists(text='发送消息…') :
                            d(text='发送消息…').send_keys('hi')
                            time.sleep(2)
                            break
                    '''


                    # 关闭输入法
                    #if d(resourceId="android:id/content").exists(timeout=1) :
                    #    d(resourceId="android:id/content").click()
                    #    time.sleep(2)

                    #xml = d.dump_hierarchy()
                    #print(xml)

                    if d(resourceId="com.ss.android.ugc.aweme:id/c1p",description='返回').exists(timeout=2) :
                        d(resourceId="com.ss.android.ugc.aweme:id/c1p",description='返回').click()
                        time.sleep(2)
                    print("-----------------------------------------------------------------------返回 1")
                    if d(resourceId="com.ss.android.ugc.aweme:id/ko",description='返回').exists(timeout=2) :
                        d(resourceId="com.ss.android.ugc.aweme:id/ko",description='返回').click()
                        time.sleep(2)
                    print("-----------------------------------------------------------------------返回 2")
                else :
                    continue
            except Exception as e1:
                continue
        ##如果没有返回
        if d(resourceId="com.ss.android.ugc.aweme:id/a81",index=str(i)).exists(timeout=3) :
            d(resourceId='com.ss.android.ugc.aweme:id/aze').click() #同城中可以，推荐中不行
        else :
            for i in(1,3) :
                if d(resourceId="com.ss.android.ugc.aweme:id/ko",description='返回').exists(timeout=2) :
                    d(resourceId="com.ss.android.ugc.aweme:id/ko",description='返回').click()
                    time.sleep(1)
                    break
            d(resourceId='com.ss.android.ugc.aweme:id/aze').click()