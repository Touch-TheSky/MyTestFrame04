# coding=utf-8
from inter.webkeys import *

http = HTTP()
http.seturl('http://112.74.191.10:80/inter/HTTP/')
http.post('auth')
http.addheader('token', http.jsonres['token'])
# 登录
http.post('login', 'username=kunkun&password=123456')
# 获取信息
http.post('getUserInfo', 'id=%s' % http.jsonres['userid'])
# 登出
http.post('logout', None)
