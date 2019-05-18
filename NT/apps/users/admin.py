from django.contrib import admin

# Register your models here.
import xadmin

from .models import UserProfile,EmailVerifyRecode


class UserProfileAdmin(object):
    list_display = ['username','password','mobile','photo','gender','updatetime','user_type']
    search_fields = ['username','password','mobile','photo','gender','updatetime','user_type']
    list_filter = ['username','password','mobile','photo','gender','updatetime','user_type']
    model_icon = 'fa fa-list'

class EmailVerifyRecodeAdmin(object):
    list_display = ['code', 'email', 'sendtype', 'createtime']
    search_fields = ['code', 'email', 'sendtype', 'updatetime']
    list_filter = ['code', 'updatetime', 'sendtype', 'createtime']
    model_icon = 'fa fa-envelope-o'


xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.unregister(UserProfile)
xadmin.site.register(EmailVerifyRecode,EmailVerifyRecodeAdmin)