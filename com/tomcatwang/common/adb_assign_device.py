# -*- coding: utf-8 -*-
import subprocess


class adb_assign_device:
    device = None

    def __init__(self,device):
        self.device = device

    def shell(self, cmd=''):
        # one-offs
        print(cmd)
        execute = subprocess.Popen("adb -s " + self.device + " %s" % cmd, shell=True, stdout=subprocess.PIPE)
        print(execute.stdout.read())
        return execute

    def input_text(self, text):
        self.shell('shell input  text {text}'.format(
            text=text))

    def key_event(self, keyword):
        self.shell(' shell input keyevent {keyword}'.format(
            keyword=keyword))

    def shell_constantly(self, cmd=''):
        # continuous monitoring
        print(cmd)
        execute = subprocess.Popen("adb %s" % cmd, shell=True, stdout=subprocess.PIPE)
        for ec in iter(execute.stdout.readline, 'b'): print(ec)
        return execute

    def version(self):
        adb_version = self.shell('version')
        return adb_version

    def logcat(self, cmd='', serial=''):
        # cmd: -s serialNumber
        android_log = self.shell_constantly('%s logcat %s' % (serial, cmd))
        return android_log

    def get_model(self, serial=''):
        # get equipment model
        screen_size = self.shell('%s shell wm getprop ro.product.model' % serial)
        return screen_size

    def get_screen_size(self, serial=''):
        # get equipment screen size
        screen_size = self.shell('%s shell wm size' % serial)
        return screen_size

    def get_density(self, serial=''):
        # get equipment density/dpi
        screen_size = self.shell('%s shell wm density' % serial)
        return screen_size

    def pull(self, equip, local='.', serial=''):
        # remote to local
        self.shell('%s pull %s %s' % (serial, equip, local))

    def push(self, local, equip, serial=''):
        # local to remote
        self.shell('%s push %s %s' % (serial, local, equip))

    def swipe(self, swipe_x1, swipe_y1, swipe_x2, swipe_y2, duration='', serial=''):
        # slide-to-unlock
        self.shell('{SID} shell input swipe {x1} {y1} {x2} {y2} {press_time}'.format(
            SID=serial, x1=swipe_x1, y1=swipe_y1, x2=swipe_x2, y2=swipe_y2,
            press_time=duration))

    def tap(self, x, y, duration='', serial=''):
        self.shell('{SID} shell input tap {x} {y} {press_time}'.format(
            SID=serial, x=x, y=y, press_time=duration))

    def long_press(self, x1, y1, x2, y2, duration, serial=''):
        # long press, minimum value is 200
        press_time = max(200, duration)
        self.swipe(x1, y1, x2, y2, press_time, serial='')
        print(press_time)
        return press_time

    def screencap(self, img, serial=''):
        # make a screen capture
        self.shell('%s shell screencap -p %s' % (serial, img))

    def get_screencap(self, img, local='.', serial=''):
        # screenshoot to local
        self. shell('%s shell screencap -p %s' % (serial, img))
        self.shell('%s pull %s %s' % (serial, img, local))

    def screenrecord(self, srd, serial=''):
        # make a screen capture
        self.shell('%s shell screenrecord %s' % (serial, srd))

    def get_screenrecord(self, srd, local='.', serial=''):
        # screenrecord to local
        self.shell('%s shell screenrecord %s' % (serial, srd))
        self.shell('%s pull %s %s' % (serial, srd, local))

    def start_app(self, package='', activity=''):
        self.shell('shell am start -n {package}/{activity}'.format(
            package=package, activity=activity))
