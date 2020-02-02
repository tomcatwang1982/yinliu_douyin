# -*- coding: utf-8 -*-


import io
device='emulator-5554'
package='com.ss.android.ugc.aweme'
d_key_string='resourceId="com.ss.android.ugc.aweme:id/ys"'
content = io.StringIO()
content.write("# -*- coding: utf-8 -*- \n")
content.write("import uiautomator2 as u2  \n")
content.write("import time  \n")
content.write("d=u2.connect('"+device+"')  \n")
content.write("d.app_start('"+package+"')  \n")
content.write("d("+d_key_string+").click() ")

fout=open('content_test.py', 'w', encoding='utf8')
# 写入文件内容
fout.write(content.getvalue())
#关闭文件
fout.close()