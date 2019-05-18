from rest_framework.permissions import BasePermission
from django.http import HttpResponse

"""访问权限的设置"""
class Mypermission(object):
    message = "必须是svip才能访问!"
    def has_permission(self,request,view):
        user_obj = request.user
        #只有svip能访问
        if user_obj.user_type !=3:
            return True
        else:
            return False