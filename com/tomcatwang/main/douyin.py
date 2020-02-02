# -*- coding: utf-8 -*-

from com.tomcatwang.db.db import Database
from com.tomcatwang.dict.db_dict import test_db_dict
from com.tomcatwang.common.log import Logger

#from reflect.conf.settings import FUNC
#from reflect.conf.settings import MODE
import importlib,re

logger = Logger().logger
m = importlib.import_module('com.tomcatwang.common.uiautomator2_cmd')
cls = m.Uiautomator2Cmd('emulator-5554')
app_start = getattr(cls,'app_start')
app_start(package_name='com.ss.android.ugc.aweme')
d_click = getattr(cls,'d_click')
d_click(resourceId="com.ss.android.ugc.aweme:id/ir")
'''
database = Database(test_db_dict)
result = database.query(
    "SELECT a.id,a.`action_id`,a.`proc_name`,a.`desc`,a.`steps`,b.type,b.`cmd`,b.`attr`,b.`pre_cmd`,b.`after_cmd` FROM `process` a INNER JOIN `action` b ON a.action_id = b.id order by a.steps asc")
if result is not None:
    logger.info('-------------------1')
    for i in result:
        logger(i)
        m = importlib.import_module('com.tomcatwang.common.uiautomator2_cmd')
        cls = getattr(m,i[''])
        response = cls().run()
'''