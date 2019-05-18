from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    user_type_choices = ((1,'普通用户')
                        ,(2,u'vip')
                        ,(3,u'svip'))


    USERNAME_FIELD = "username"

    GENDER_CHOISE = (('M', u'男'), ('F', '女'))
    gender = models.CharField(verbose_name='性别', choices=GENDER_CHOISE, max_length=1, default='M')
    mobile = models.CharField(verbose_name='手机号码', max_length=11, null=True, blank=True)
    photo = models.ImageField(verbose_name='头像',upload_to='Headportrait', max_length=500)
    updatetime = models.DateField(verbose_name='更新时间', auto_now=True)
    createtime = models.DateField(verbose_name='创建时间', auto_now_add=True)
    user_type = models.IntegerField(verbose_name="用户权限",choices=user_type_choices,default=1)
    class Meta:
        app_label = 'users'
        verbose_name = u'用户'
        verbose_name_plural = verbose_name
        db_table = 'user_profile'
        ordering = ['-updatetime']

    def __str__(self):
        return self.username




class EmailVerifyRecode(models.Model):
    TYPE_CHOICES = (
		('register', u'注册'),
		('forget', u'找回密码')
	)
    code = models.CharField(verbose_name='验证码', max_length=20)
    email = models.EmailField(verbose_name='邮箱', max_length=50)
    sendtype = models.CharField(verbose_name='验证码类型', max_length=20, choices=TYPE_CHOICES)
    updatetime = models.DateField(verbose_name='更新时间', auto_now=True)
    createtime = models.DateField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        app_label = 'users'
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
        db_table = 'email_verify_recode'

    def __unicode__(self):
        return self.code





























