import time
from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
from django.core.cache import cache
VISIT_RECORD ={}

class VisitThrottle(SimpleRateThrottle):
    """调用restframework内置节流器"""
    scope = 'laoli'

    def get_cache_key(self, request, view):
        return self.get_ident(request)




class MyThrottle(BaseThrottle):
    """自定义的节流器先验证token然后验证匿名用户ip"""
    def __init__(self):
        self.history = None

    def allow_request(self,request,view):
        # self.history = None
        remote_addr = request.META.get('REMOTE_ADDR')
        token = request._request.GET.get('token')
        ctime = time.time()
        if token:#token方式节流
            if token not in VISIT_RECORD:
                VISIT_RECORD[token] = [ctime, ]
                return True
            history = VISIT_RECORD.get(token)
            self.history = history

            while history and history[-1] < ctime-60:
                history.pop()
            if len(history) < 5:#更改一分内钟访问次数
                history.insert(0,ctime)
                print(cache.get(token))
                return True
            else:
                return False

        elif remote_addr:#IP方式节流
            if remote_addr not in VISIT_RECORD:
                VISIT_RECORD[remote_addr] = [ctime,]
                return True
            history = VISIT_RECORD.get(remote_addr)
            self.history = history

            while history and history[-1] < ctime-60:
                history.pop()
            if len(history) < 5:#更改一分内钟访问次数
                history.insert(0,ctime)
                return True
            else:
                return False

    def wait(self):
        ctime = time.time()
        return  60 - (ctime-self.history[-1])

