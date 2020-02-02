# -*- coding: utf-8 -*-

import uiautomator2 as u2

d = u2.connect('192.168.3.8:5555')

d.app_start("com.ss.android.ugc.aweme")
