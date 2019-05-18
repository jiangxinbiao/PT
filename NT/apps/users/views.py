from rest_framework.views import APIView
from users.user_servic.user_server import UserServic
from django.http import HttpResponse
# from rest_framework import mixins
# from rest_framework.generics import GenericAPIView,ListAPIView
# from .serializers import UserSerializer
# from .models import UserProfile
from wsgiref.simple_server import make_server
from django.shortcuts import render
class EmailVerifyRecodeView(APIView):
    authentication_classes = []
    permission_classes = []
    def login(self,request,*args,**kwargs):
        pass
    def register(self,*args,**kwargs):
        pass
    def get(self,*args,**kwargs):
        pass
    def delete(self,*args,**kwargs):
        pass

class RegisterView(UserServic):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        content = super(RegisterView, self).register(request=request)
        return content


#完成认证的添加和token的分发
class Loginview(UserServic):
    """登录认证中生成token"""
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        content = super(Loginview,self).login(request=request)
        return content

class Userlistview(UserServic):
    """登录认证中生成token"""
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        content = super(Userlistview,self).get(request=request)
        return content

class UserPut(UserServic):
    """登录认证中生成token"""
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        content = super(UserPut,self).put(request=request)
        return content

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request,'register.html')
def forget(request):
    return render(request,'forget.html')
def revise(request):
    return render(request,'chongshemima.html')
class Resetview(UserServic):
    """登录认证中生成token"""
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        content = super(Resetview,self).reset(request=request)
        return content