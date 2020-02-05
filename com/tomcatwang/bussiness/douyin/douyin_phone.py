# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time, re
from com.tomcatwang.common.adb import swipe, tap
from com.tomcatwang.common.log import Logger
from com.tomcatwang.common.douyin_init import douyin_init

##########################################################################
'''
参数设置
'''
logger = Logger()
# loop video num 需要循环观看多少个视频
loop_video_num = 50
loop_message_num = 5
hua_su = 'hi,你好,能加个好友聊聊吗?'
douyin_start_time = 8
##########################################################################
##抖音視頻翻頁##
page_down_x1 = 501
page_down_y1 = 1819
page_down_x2 = 497
page_down_y2 = 265
device = '7460300e'
###########################################################################
'''
func def
'''
##日志##
def log():
    return Logger().logger


def return_pre_page():
    #if d(resourceId="com.ss.android.ugc.aweme:id/c1p", description='返回').exists(timeout=2):
    #    d(resourceId="com.ss.android.ugc.aweme:id/c1p", description='返回').click()
    #    logger.info("返回操作..............................................................1")
    #else:
    logger.info("返回操作..............................................................")
    tap(61, 143)

'''
检测当前的页面
'''
def check_is_user_guanzhu_page():
    if (d(text="取消关注").exists() or d(text="相互关注").exists() or d(text="正在请求")):
        logger.info("在用户关注页面，需要返回")
        return_pre_page()
        logger.info("返回视频留言页面..............................................................")


def is_user_vieo_page():
    if d.exists(resourceId='com.ss.android.ugc.aweme:id/zc'):
        logger.info("在用户视频页面")
        return True
    else:
        return False

# com.ss.android.ugc.aweme.main.MainActivity
##start atx
# d.app_start("com.github.uiautomator","com.github.uiautomator.MainActivity")
# d(resourceId="com.github.uiautomator:id/start_uiautomator").click()
# xml = d.dump_hierarchy()
# 关闭输入法
# if d(resourceId="android:id/content").exists(timeout=1) :
#    d(resourceId="android:id/content").click()
#    time.sleep(2)
# xml = d.dump_hierarchy()
# print(xml)
# print(xml)
# emulator-5554
# d3cf3594 oppo
# 7460300e xiaomi
##connect device
# '192.168.3.12:5555'
# 192.168.1.119:5555
# 192.168.3.8:5555
# d = u2.connect('192.168.1.119:5555')

logger.info("连接手机.............................................................." + str(device))
d = u2.connect(device)
logger.info("程序初始化......................................................................")
douyin_init(d)
logger.info("启动抖音程序....................................................................")

try:
    for j in range(0, loop_video_num):
        # loop message num 需要循环多少个留言用户
        loop_message_num_per = loop_message_num
        # pagedown,上滑，视频翻页
        swipe(page_down_x1, page_down_y1, page_down_x2, page_down_y2)
        swipe(page_down_x1, page_down_y1, page_down_x2, page_down_y2)
        swipe(page_down_x1, page_down_y1, page_down_x2, page_down_y2)
        if not is_user_vieo_page:
            logger.info("第" + str(j) + "个视频,不是视频页面，可能是直播或者其他页面.............................")
            continue
        # loop wait message button appear 点击回复按钮
        if d.exists(resourceId='com.ss.android.ugc.aweme:id/zc'):
            logger.info("第" + str(j) + "个视频..................................................................")
            logger.info("点击回复按钮....................................................................")
            d(resourceId='com.ss.android.ugc.aweme:id/zc').click()

            ##get ping lun shu
            try:
                if not d(resourceId='com.ss.android.ugc.aweme:id/a50').exists(timeout=1):
                    logger.info("留言数为0....................................................................")
                    tap(161, 143)
                    logger.info("留言数为0，会提示输入留言，关闭留言窗口......................................")
                    d(resourceId='com.ss.android.ugc.aweme:id/aze').click()
                    logger.info("留言数为0，关闭留言窗口......................................................")
                    continue

                message_total = str((d(resourceId='com.ss.android.ugc.aweme:id/a50').info['contentDescription']))
                str_ping_lun_total = re.findall("([1-9]+)", message_total)[0]
                logger.info(
                    "str_ping_lun_total............................................------>:" + str_ping_lun_total)

                if (str_ping_lun_total != '' and str_ping_lun_total.rfind('w') > 0):
                    str_ping_lun_total = str_ping_lun_total.replace(str_ping_lun_total, 'w', '0000')
                    int_ping_lun_total = int(float(str_ping_lun_total) * 10000)
                else:
                    int_ping_lun_total = int(str_ping_lun_total)
            except Exception as e:
                print(e)
                logger.error("留言数异常......................................................................")
                int_ping_lun_total = 0
                if d(resourceId='com.ss.android.ugc.aweme:id/aze').exists(timeout=1):
                    d(resourceId='com.ss.android.ugc.aweme:id/aze').click()  # 同城中可以，推荐中不行
                else:
                    tap(194, 424)
                logger.error("留言数异常,关闭留言窗口.........................................................")

            logger.info(
                "留言数量是...............................................................--->:" + str(int_ping_lun_total))
            ###message num if > 0

            try:
                if (int_ping_lun_total > 0):
                    if (int_ping_lun_total <= loop_message_num_per):
                        logger.info("如果设定的用户留言数大于整个留言数....................................................")
                        # if message num < 设定的评论数
                        loop_message_num_per = int_ping_lun_total

                    good_num = 0
                    bad_mum = 0
                    i = 0
                    while True :
                        logger.info("第" + str(
                            i) + "个有用户留言..................................................................")

                        if (good_num == loop_message_num_per or (i >= loop_message_num_per)) :
                            break

                        try:
                            if (d(resourceId="com.ss.android.ugc.aweme:id/a81", index=str(i)).exists(timeout=1.5)\
                                   or d(resourceId="com.ss.android.ugc.aweme:id/bzo", index=str(i)).exists(timeout=1)):

                                if (d(resourceId="com.ss.android.ugc.aweme:id/a81", index=str(i)).exists(timeout=0.7)) :
                                    d(resourceId="com.ss.android.ugc.aweme:id/a81", index=str(i)).child(
                                        resourceId="com.ss.android.ugc.aweme:id/bzo").child(
                                        resourceId="com.ss.android.ugc.aweme:id/jo").click()
                                elif (d(resourceId="com.ss.android.ugc.aweme:id/bzo", index=str(i)).exists(timeout=0.7)) :
                                    d(resourceId="com.ss.android.ugc.aweme:id/bzo", index=str(i)).child(
                                        resourceId="com.ss.android.ugc.aweme:id/a81").child(
                                        resourceId="com.ss.android.ugc.aweme:id/jo").click()

                                time.sleep(0.7)

                                if (d(text="取消关注").exists() or d(text="相互关注").exists() or d(text="正在请求")):
                                    logger.info("第" + str(
                                        i) + "个有用户已经关注了或者需要请求，返回......................................................")
                                    return_pre_page()
                                    i = i + 1
                                    continue

                                time.sleep(0.5)

                                if d(resourceId='com.ss.android.ugc.aweme:id/axp').exists(timeout=1):
                                    logger.info("com.ss.android.ugc.aweme:id/axp第" + str(
                                        i) + "个有用户异常，返回....................................................................")
                                    return_pre_page()
                                    i = i + 1
                                    continue

                                time.sleep(0.5)

                                if d(text="关注").exists(timeout=1):
                                    logger.info(
                                        "关注第" + str(i) + "个有用户......................................................")
                                    d(text="关注").click()
                                else:  # 如果没有关注就返回
                                    logger.info(
                                        "关注第" + str(i) + "个有用户不成功................................................")
                                    return_pre_page()
                                    i = i + 1
                                    continue

                                time.sleep(0.7)

                                if d(text="私信").exists(timeout=1):
                                    d(text='私信').click()
                                    logger.info(
                                        "私信第" + str(i) + "个有用户......................................................")
                                    time.sleep(1)
                                else:  # 如果没有私信就返回
                                    logger.info(
                                        "私信第" + str(i) + "个有用户不成功................................................")
                                    return_pre_page()
                                    i = i + 1
                                    continue

                                time.sleep(0.7)

                                if d(text="发送消息…").exists(timeout=0.5):
                                    logger.info(
                                        "私信第" + str(i) + "个用户......................................................")
                                    d(text="发送消息…").send_keys(hua_su)
                                    time.sleep(1.2)

                                if d(description="发送").exists(timeout=0.5):
                                    d(description="发送").click()
                                    time.sleep(1.2)

                                return_pre_page()
                                logger.info(
                                    "返回第" + str(i) + "个用户关注页面...................................................")

                                return_pre_page()
                                logger.info(
                                    "返回用户视频留言页面...................................................")

                                logger.info("完成第"+str(i)+"用户关注---------------------------------------------------------------end\n")
                                good_num = good_num + 1
                                i = i + 1
                            else:
                                bad_mum = bad_mum + 1
                                logger.info(
                                    "点击第" + str(i) + "个用户出现异常...................................................")
                                i = i + 1
                                #return_pre_page()
                                continue
                        except Exception as e1:
                            bad_mum = bad_mum + 1
                            logger.info(
                                "点击第" + str(i) + "个用户出现异常...........................continue....................")
                            i = i + 1
                            logger.error(e1)
                            continue


                    ##查询当前页面##
                    check_is_user_guanzhu_page()

                    if d(resourceId='com.ss.android.ugc.aweme:id/aze').exists(timeout=1):  # 同城中可以，推荐中不行
                        d(resourceId='com.ss.android.ugc.aweme:id/aze').click()
                    else:
                        d.click(442, 413)

                    logger.info("完成第"+str(j)+"视频-----------------------------------------------------------------------------end\n")

                    time.sleep(1)
            except Exception as e2:
                logger.error(e2)
                continue

except Exception as e:
    logger.info("最外层程序异常...................................................")
    logger.error(e)
