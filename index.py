# coding: utf-8
'''
@author: sy-records
@license: https://github.com/sy-records/v-checkin/blob/master/LICENSE
@contact: 52o@qq52o.cn
@desc: 腾讯视频好莱坞会员V力值签到，支持两次签到：一次正常签到，一次手机签到。
@blog: https://qq52o.me
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

auth_refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=1466058336&g_vstk=119256359&g_actk=&callback=jQuery19108448546588656134_1608110455183&_=1608110455184'
sckey = 'SCU128438T4f054b96177e8e2db79141d37baf73635fb868c1079cb'

ftqq_url = "https://sc.ftqq.com/%s.send"%(sckey)
url1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'
url2 = 'https://v.qq.com/x/bu/mobile_checkin'

login_headers = {
    'Referer': 'https://v.qq.com',
    'Cookie': 'pgv_pvi=5326982144; RK=cR7028CSNi; ptcz=535ad09d6aaafa8ef362864f97b587d3293bf353c41e0ad395814c7dd8f796f7; pgv_pvid=7826914100; tmeLoginType=2; psrf_qqrefresh_token=B1D34AE6B046BD631F4001604A78755F; psrf_access_token_expiresAt=1614361931; psrf_qqopenid=43E8378ADE3414AE1ACDA9462F33EFEA; psrf_qqaccess_token=7E57984F0DE828254084F90C3318BB68; euin=oinsoK4loi4*; psrf_qqunionid=; video_guid=9e3c7df5c6564d8a; video_platform=2; luin=o0030615735; lskey=00010000b39b06f087a10b53a57285d6ef90f641e1c6a61d41da7074b4c829efb4cd06f1c4c475c83bb333b9; main_login=qq; vuserid=230176592; login_time_init=1607191996; _video_qq_version=1.1; _video_qq_main_login=qq; _video_qq_appid=3000501; _video_qq_vuserid=230176592; _video_qq_login_time_init=1607191996; o_cookie=30615735; pac_uid=1_30615735; tvfe_boss_uuid=d7b0bb7e65959930; vusession=iP6LgADp7FARcaL1i-Wzpg..; _video_qq_vusession=iP6LgADp7FARcaL1i-Wzpg..; pgv_info=ssid=s1418259800; uid=421497017; pgv_si=s6366426112; _qpsvr_localtk=0.5408190187791031; next_refresh_time=3072; _video_qq_next_refresh_time=3072; login_time_last=2020-12-16 17:20:40'
}

login = requests.get(auth_refresh_url, headers=login_headers)
cookie = requests.utils.dict_from_cookiejar(login.cookies)

if not cookie:
    print "auth_refresh error"
    payload = {'text': '腾讯视频V力值签到通知', 'desp': '获取Cookie失败，Cookie失效'}
    requests.post(ftqq_url, params=payload)

sign_headers = {
    'Cookie': 'pgv_pvi=5326982144; RK=cR7028CSNi; ptcz=535ad09d6aaafa8ef362864f97b587d3293bf353c41e0ad395814c7dd8f796f7; pgv_pvid=7826914100; tmeLoginType=2; psrf_qqrefresh_token=B1D34AE6B046BD631F4001604A78755F; psrf_access_token_expiresAt=1614361931; psrf_qqopenid=43E8378ADE3414AE1ACDA9462F33EFEA; psrf_qqaccess_token=7E57984F0DE828254084F90C3318BB68; euin=oinsoK4loi4*; psrf_qqunionid=; video_guid=9e3c7df5c6564d8a; video_platform=2; luin=o0030615735; lskey=00010000b39b06f087a10b53a57285d6ef90f641e1c6a61d41da7074b4c829efb4cd06f1c4c475c83bb333b9; main_login=qq; vuserid=230176592; login_time_init=1607191996; _video_qq_version=1.1; _video_qq_main_login=qq; _video_qq_appid=3000501; _video_qq_vuserid=230176592; _video_qq_login_time_init=1607191996; o_cookie=30615735; pac_uid=1_30615735; tvfe_boss_uuid=d7b0bb7e65959930; vusession=iP6LgADp7FARcaL1i-Wzpg..; _video_qq_vusession=iP6LgADp7FARcaL1i-Wzpg..; pgv_info=ssid=s1418259800; uid=421497017; pgv_si=s6366426112; _qpsvr_localtk=0.5408190187791031; next_refresh_time=3072; _video_qq_next_refresh_time=3072; login_time_last=2020-12-16 17:20:40'] + ';',
    'Referer': 'https://m.v.qq.com'
}
def start():
  sign1 = requests.get(url1,headers=sign_headers).text
  if 'Account Verify Error' in sign1:
    print 'Sign1 error,Cookie Invalid'
    status = "链接1 失败，Cookie失效"
  else:
    print 'Sign1 Success'
    status = "链接1 成功，获得V力值：" + sign1[42:-14]

  sign2 = requests.get(url2,headers=sign_headers).text
  if 'Unauthorized' in sign2:
    print 'Sign2 error,Cookie Invalid'
    status = status + "\n\n 链接2 失败，Cookie失效"
  else:
    print 'Sign2 Success'
    status = status + "\n\n 链接2 成功"

  payload = {'text': '腾讯视频V力值签到通知', 'desp': status}
  requests.post(ftqq_url, params=payload)

def main_handler(event, context):
  return start()
if __name__ == '__main__':
  start()
