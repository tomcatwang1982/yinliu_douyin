# -*- coding: utf-8 -*-
import uiautomator2 as u2

d = u2.connect('2529b8a80906')
xml = d.dump_hierarchy()
print(xml)