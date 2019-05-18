from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from django.utils import timezone
from datetime import timedelta
from rest_framework.authentication import BaseAuthentication
from django.core.cache import cache



#验证可用！！！！！！
class Authtication(BaseAuthentication):

    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = Token.objects.filter(key = token).first()
        if not token_obj:
            raise  exceptions.AuthenticationFailed('用户认证失败')
        if timezone.now() > (
                token_obj.created + timedelta(days=5 )):
            # 重点就在这句了，这里做了一个Token过期的验证 timedelta(microseconds)，如果当前的时间大于Token创建时间+DAYS天，那么久返回Token已经过期
            raise exceptions.AuthenticationFailed(_('登录已过期！麻烦重新登录！'))
        return  (token_obj.user,token_obj)
    def authenticate_header(self,request):
        pass


class NewAuthtication(BaseAuthentication):
    pass
