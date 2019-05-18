
from django.conf.urls import url,include
from Paintings.views import PaintingView,CommentsView,Labelview,IndexView
from rest_framework import routers

"""全自动生成url"""
router = routers.DefaultRouter()
router.register(r'Painting',PaintingView)

urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/Comments/',CommentsView.as_view({'get': 'list'}),name='Comments'),
    url(r'^(?P<version>[v1|v2]+)/Labels/',Labelview.as_view({'get': 'list'}),name='Labels'),
    url(r'^(?P<version>[v1|v2]+)/Painting/(?P<pk>\d+)/$',PaintingView.as_view({'get':'list','post':'create','delete':'destroy','put':'update'}),name='pt'),
    # url(r'^(?P<version>[v1|v2]+)/',include(router.urls))
    url(r'^index/',IndexView.as_view(), name='index'),
]