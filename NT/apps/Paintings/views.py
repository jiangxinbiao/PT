from django.http import HttpResponse
from Paintings.serializers import PaintingSerializer,CommentSerializer,LabelSerializer
from Paintings.models import Painting,Comments,Label
from Paintings.models import AdminIMG #富文本编辑器的图片模型
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from .Paintings_servic.PageNumber import MyPageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from django.shortcuts import render
    # ListModelMixin        获取全部资源（列表）
    # CreateModelMixin      创建资源
    # RetrieveModelMixin    获取单条数据
    # UpdateModelMixin      更新一个资源
    # DestoryModelMixin     删除一个资源

"""标签类视图"""
class Labelview(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    authentication_classes = []
    permission_classes = []

    # 查询结果集
    queryset = Label.objects.all()
    # 序列化器类
    serializer_class = LabelSerializer

    pagination_class = PageNumberPagination
    def throttled(self, request, wait):
        from rest_framework.exceptions import Throttled
        class VisitThrottle(Throttled):
            default_detail = '请耐心等待'
            extra_detail_singular = '还有 {wait} second.'
            extra_detail_plural = '快了还有 {wait} 秒 就能再次访问！'

        raise VisitThrottle(wait)


"""作品类视图"""
class PaintingView(mixins.ListModelMixin
                   ,mixins.CreateModelMixin
                   ,mixins.RetrieveModelMixin
                   ,mixins.DestroyModelMixin
                   ,mixins.UpdateModelMixin
                   ,GenericViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Painting.objects.all()
    """序列化器类"""
    serializer_class = PaintingSerializer

    pagination_class = PageNumberPagination

    def throttled(self, request, wait):
        from rest_framework.exceptions import Throttled
        class VisitThrottle(Throttled):
            default_detail = '请耐心等待'
            extra_detail_singular = '还有 {wait} second.'
            extra_detail_plural = '快了还有 {wait} 秒 就能再次访问！'

        raise VisitThrottle(wait)



"""评论类视图"""
class CommentsView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):

    # 查询结果集
    queryset =Comments.objects.all()
    # 自动序列化器类
    serializer_class = CommentSerializer
    authentication_classes = []
    permission_classes = []

    def throttled(self, request, wait):
        from rest_framework.exceptions import Throttled
        class VisitThrottle(Throttled):
            default_detail = '请耐心等待'
            extra_detail_singular = '还有 {wait} second.'
            extra_detail_plural = '快了还有 {wait} 秒 就能再次访问！'

        raise VisitThrottle(wait)

class IndexView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')



#富文本编辑器图片储存问题未解决！！！！！！！！！！！！！！！！！！！！！！！！！！！！
def uploadIMG(request):
    img = request.FILES.get('img')
    adminIMG = AdminIMG()
    adminIMG.filename = img.name
    adminIMG.img = img
    adminIMG.save()
    return HttpResponse(
                "<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('/media/%s')."
                "closest('.mce-window').find('.mce-primary').click();</script>" % adminIMG.img)





















