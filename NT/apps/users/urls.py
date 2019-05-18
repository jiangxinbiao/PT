
from django.conf.urls import url,include
from .import views
from .views import EmailVerifyRecodeView,Loginview,RegisterView,Userlistview,UserPut,register,forget,revise,Resetview,login



urlpatterns = [
    url(r'^DoLogin/', Loginview.as_view(),name='DoLogin'),
    url(r'^EmailVerifyRecode/',EmailVerifyRecodeView.as_view(),name='EmailVerifyRecode'),
    url(r'^Register/', RegisterView.as_view(),name='Register'),
    url(r'^Userlist/', Userlistview.as_view(),name='Userlist'),#UserPut
    url(r'^UserPut/', UserPut.as_view(),name='UserPut'),
    url(r'^login/',login,name = 'login'),
    url(r'^register/',register,name = 'register'),
    url(r'^forget/',forget,name = 'forget'),
    url(r'^revise/',revise,name = 'revise'),
    url(r'^Resetview/',Resetview.as_view(),name = 'Resetview'),

]