# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time, requests
from com.tomcatwang.common.adb import swipe, tap

headers = {
    'X-SS-REQ-TICKET': '1581143111595',
    'sdk-version': '1',
    'Cookie': 'tt_webid=a87d38eca27a52b84524e9b7a159af48; d_ticket=a4fad96f751f52ebb639fd66ee22dcc10f2c5; odin_tt=b643a40d55aeb414dbb8f3f8eec658b60b75f5510f5cda4f35aec2496aeb3af3deb0aefa8e44261c63a696f3e6383419; msh=pwitenR2dWzO4fuAoSoyqAsMihw; install_id=96236324401; ttreq=1$69fba9c4f167bd26218c4c7c96a4a7dacba0f371; sid_guard=b412c6d99a5c6d2b06dcf8a2ea8a0786%7C1581127954%7C5184000%7CWed%2C+08-Apr-2020+02%3A12%3A34+GMT; uid_tt=903eaf8b9056d4c49cc42658dc616683; sid_tt=b412c6d99a5c6d2b06dcf8a2ea8a0786; sessionid=b412c6d99a5c6d2b06dcf8a2ea8a0786',
    'x-tt-token': '00b412c6d99a5c6d2b06dcf8a2ea8a078648937eeaaf9e369a434d8245741b06a5cca685072a5d26446574e5d19d9dce4652',
    'X-Gorgon': '030000004005e4694457d6e0ddbfb7a4dbadbc7e0663451d5f4e',
    'X-Khronos': '1581143111',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.87 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
}

search_url = 'https://aweme-lq.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&sec_user_id=MS4wLjABAAAAyyzyFDmccTkbhCMqAq1__IuRVuV0O8dnoBABvUgQ3_w&count=20&retry_type=no_retry&iid=96236324401&device_id=39531304211&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=840&version_name=8.4.0&device_platform=android&ssmix=a&device_type=r8207&device_brand=oppo&language=zh&os_api=22&os_version=5.1.1&uuid=865166025762330&openudid=a95bb4e3a52338bd&manifest_version_code=840&resolution=1600*900&dpi=240&update_version_code=8402&_rticket=1581143111578&mcc_mnc=46000&ts=1581150575&app_type=normal&_signature=QOtJJBARHVwzHUNLqlT-mEDrST&dytk=593d265a74e3384e06112b423ef268da'
req = requests.get(url=search_url, verify=False, headers=headers)
print(req.text)
