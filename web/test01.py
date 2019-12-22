# -*- coding: UTF-8 -*-
from web.keywordOfWeb import KeywordOfWeb

kw = KeywordOfWeb()
# 打开浏览器
kw.openBrower()
# 打开网页
kw.geturl("http://112.74.191.10:8000/")
kw.halt(3)
# 登录
kw.click("//a[text()='登录']")
kw.input("//input[@name='username']","1119778030@qq.com")
kw.input("//input[@name='password']","123456")
kw.input("//input[@name='verify_code']",1)
kw.click("//a[@name='sbtbutton']")
kw.halt(2)
# 校验
kw.gettext("//a[text()='返回商城首页']")
kw.asserteqiue("返回商城首页","登录")
kw.quit()













