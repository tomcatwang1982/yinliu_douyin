# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
import multiprocessing as np
import subprocess
from com.tomcatwang.bussiness.douyin.douyin_phone import execute


def getphonelist():  # 获取手机设备
    cmd = r'adb devices'  # % apk_file
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()  # 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    devices = []
    for i in (out)[1:-1]:
        device = str(i).split("\\")[0].split("'")[-1]
        print(device)
        devices.append(device)
    return devices  # 手机设备列表

def MultiDevice(d):  # 功能执行
    execute(d)

def execute_process(i):  #执行用例
    MultiDevice(getphonelist()[int(i)])

def main():#多进程
    print(len(getphonelist()))
    for i in range(len(getphonelist())):  #有几个设备起几个进程
        p = np.Process(target=execute_process, args=(str(i)))
        p.start()

if __name__ == '__main__':
    main()