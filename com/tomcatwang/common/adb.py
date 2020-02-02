# -*- coding: utf-8 -*-
import subprocess

def shell(cmd=''):
    # one-offs
    print(cmd)
    execute = subprocess.Popen("adb %s"%cmd, shell=True, stdout=subprocess.PIPE)
    print(execute.stdout.read())
    return execute

def input_text(text):
    shell('shell input  text {text}'.format(
        text=text))

def key_event(keyword) :
    shell(' shell input keyevent {keyword}'.format(
        keyword=keyword))

def shell_constantly(cmd=''):
    # continuous monitoring
    print(cmd)
    execute = subprocess.Popen("adb %s"%cmd, shell=True, stdout=subprocess.PIPE)
    for ec in iter(execute.stdout.readline, 'b'): print(ec)
    return execute

def version():
    adb_version = shell('version')
    return adb_version

def logcat(cmd='', serial=''):
    # cmd: -s serialNumber
    android_log = shell_constantly('%s logcat %s'%(serial,cmd))
    return android_log

def get_model(serial=''):
    # get equipment model
    screen_size = shell('%s shell wm getprop ro.product.model'%serial)
    return screen_size

def get_screen_size(serial=''):
    # get equipment screen size
    screen_size = shell('%s shell wm size'%serial)
    return screen_size

def get_density(serial=''):
    # get equipment density/dpi
    screen_size = shell('%s shell wm density'%serial)
    return screen_size

def pull(equip, local='.', serial=''):
    # remote to local
    shell('%s pull %s %s'%(serial, equip, local))

def push(local, equip, serial=''):
    # local to remote
    shell('%s push %s %s'%(serial, local, equip))

def swipe(swipe_x1, swipe_y1, swipe_x2, swipe_y2, duration='', serial=''):
    # slide-to-unlock
    shell('{SID} shell input swipe {x1} {y1} {x2} {y2} {press_time}'.format(
        SID=serial, x1=swipe_x1, y1=swipe_y1, x2=swipe_x2, y2=swipe_y2,
        press_time=duration))

def tap(x,y,duration='',serial=''):
    shell('{SID} shell input tap {x} {y} {press_time}'.format(
        SID=serial, x=x, y=y,press_time=duration))

def long_press(x1, y1, x2, y2, duration, serial=''):
    # long press, minimum value is 200
    press_time = max(200, duration)
    swipe(x1, y1, x2, y2, press_time, serial='')
    print(press_time)
    return press_time

def screencap(img, serial=''):
    # make a screen capture
    shell('%s shell screencap -p %s'%(serial, img))

def get_screencap(img, local='.', serial=''):
    # screenshoot to local
    shell('%s shell screencap -p %s'%(serial, img))
    shell('%s pull %s %s'%(serial, img, local))

def screenrecord(srd, serial=''):
    # make a screen capture
    shell('%s shell screenrecord %s'%(serial, srd))

def get_screenrecord(srd, local='.', serial=''):
    # screenrecord to local
    shell('%s shell screenrecord %s'%(serial, srd))
    shell('%s pull %s %s'%(serial, srd, local))

def start_app(package='',activity=''):
    shell('shell am start -n {package}/{activity}'.format(
        package=package,activity=activity))