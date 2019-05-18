from users.models import UserProfile
from rest_framework import exceptions
from django.http import JsonResponse
from django.contrib.auth.hashers import  check_password,make_password
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from django.shortcuts import HttpResponse,render
from rest_framework.authtoken.models import Token
from users.serializers import UserSerializer,EmailVerifyRecodeSerializer
from rest_framework.response import Response
from django.core.mail import send_mail,EmailMultiAlternatives,EmailMessage
from django.conf import settings
import templates
from django.template import Context, loader

class UserServic(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 GenericAPIView):
    authentication_classes = []
    permission_classes = []
    # throttle_classes = []

    queryset = UserProfile.objects.all()
    # 序列化器类
    serializer_class = UserSerializer
    def login(self,request):
        ret = {'code': 1000, 'msg': "登录成功", 'token': None}
        user = request.POST.get("username")
        pwd  = request.POST.get("password")
        # user = 'jiang'
        # pwd = 'jianghan'
        print(user, pwd)
        # print(request.body)
        # print(request.data)
        try:
            obj = UserProfile.objects.filter(username=user).first()# member.
            if obj is None:
                ret['code'] = 1001
                ret['msg'] = "用户名错误!"
                return JsonResponse(ret)
            else:
                """登录认证中生成token"""
                pw = check_password(pwd,obj.password)
                if pw:
                    try:
                        token = Token.objects.get(user=obj)
                        token.delete()
                        token = Token.objects.create(user=obj)
                        ret['code'] = 1000
                        ret['token'] = token.key
                        ret['msg']   = "登录成功"
                        return JsonResponse(ret)
                    except:
                        return HttpResponse("生成token出错！")
                else:
                    ret['code'] = 1001
                    ret['msg'] = "密码错误!"
                    return JsonResponse(ret)
        except:
            ret['code'] = 1002
            ret['msg'] = "请求异常或者用户已登录，如需再次登录请先注销！"
            return JsonResponse(ret)

    def register(self,request,*args,**kwargs):
        ret = {'code': 1000, 'msg': "邮件发送成功"}
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(username,email,password)
        same_name_user = UserProfile.objects.filter(username=username).first()
        same_email_user = UserProfile.objects.filter(email=email).first()
        if same_email_user:  # 邮箱地址唯一
            ret['code'] = 1001
            ret['msg'] = '该邮箱已注册，请重新输入邮箱！'
            return JsonResponse(ret)
        if same_name_user:  # 用户名唯一
            ret['code'] = 1001
            ret['msg'] = '用户名已存在，请另选其他用户名！'
            return JsonResponse(ret)
        new_user = UserProfile.objects.create_user(username=username)
        new_user.username = username
        new_user.password = make_password(password)
        new_user.email = email
        new_user.save()
        ret['code'] = 1000
        ret['msg'] = '注册成功！'
        return JsonResponse(ret)

    def get(self,request,*args,**kwargs):
        return self.list(request)
        # pass
    def put(self,request,*args,**kwargs):
        ret = {'code': 1000, 'msg': "邮件发送成功"}
        username = request.POST.get('username')
        email = request.POST.get('email')
        print(username,email)
        same_name_user = UserProfile.objects.filter(username=username).first()
        same_email_user = UserProfile.objects.filter(email=email).first()
        print(same_name_user,same_email_user)
        if same_name_user is None:  # 验证邮箱
            ret['code'] = 1001
            ret['msg'] = "查询不到该用户!"
            return JsonResponse(ret)
        elif same_email_user is None:
            ret['code'] = 1001
            ret['msg'] = "邮箱错误或者为空!"
            return JsonResponse(ret)
        msg = '测试:http://127.0.0.1:8000/users/revise/'
        print("第三步成功")
        try:
            send_mail(
                '测试邮件！',
                msg,
                settings.EMAIL_HOST_USER,
                [email]
            )
            print("邮件发送成功！")
            ret['code'] = 1000
            ret['msg'] = "邮件发送成功！"
            return JsonResponse(ret)
        except:
            message = "邮件发送失败！"
            print("失败")
            raise exceptions.AuthenticationFailed(message)

    def reset(self,request,*args,**kwargs):
        ret = {'code': 1000, 'msg': ""}
        use = request.POST.get("username")
        pwd = request.POST.get('password')
        print(use,pwd)
        if use and pwd is not None:
            t = UserProfile.objects.filter(username=use).first()
            print(t.id)
            if t:
                t.password = make_password(pwd)
                t.is_active=True
                t.save()
                ret['code'] = 1000
                ret['msg'] = "密码修改成功！"
                return JsonResponse(ret)
        else:
            ret['code'] = 1001
            ret['msg'] = "用户名错误！"
            return JsonResponse(ret)
    def throttled(self, request, wait):
        from rest_framework.exceptions import Throttled
        class VisitThrottle(Throttled):
            default_detail = '请耐心等待'
            extra_detail_singular = '还有 {wait} second.'
            extra_detail_plural = '快了还有 {wait} 秒 就能再次访问！'

        raise VisitThrottle(wait)