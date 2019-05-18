#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'cpy'


class Config(object):
    # 日志名称：
    BUSINESS = 'blog'
    AUTHOR = 'author'

    PAGINATION_NUM = 4

    AJAX_SUCCESSFUL_CODE = 200
    AJAX_NOTFOUND_CODE = 404
    AJAX_INVALID_CODE = 500

    AJAX_SUCCESSFUL_MSG = u'successful'
    AJAX_INVALID_MSG = u'form is invalid..'

    # 邮箱验证相关
    SMTPSERVER = 'smtp.qq.com'
    EMAIL_FROM = '102272702@qq.com'
    EMAIL_PORT = 465
    EMIAL_USER = 'jwhbios@qq.com'
    EMAIL_PASSWORD = 'fxtiuinwazctbibi'

    EMAIL_TITLE = u'注册激活链接'
    EMAIL_Prompt = u'请点击下面的链接激活你的账号,如非本人操作请忽略:'
    EMAIL_BODY = u"http://127.0.0.1:8000/user/active/"
    # 验证码相关
    DEFAULT_RANDOM_LENGTH = 16
    RANDOM_CHAR = u'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    DEFAULT_SENDTYPE = u'register'
    FORGET_SENDTYPE = u'forget'

    SEND_SUCCESSFUL = u'邮件发送成功'
    SEND_INVALID = u'邮件发送失败'