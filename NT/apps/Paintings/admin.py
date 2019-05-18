from django.contrib import admin
import xadmin
# Register your models here.
from Paintings.models import Painting,Label,Comments,AdminIMG


class PaintingAdmin(object):
    list_display = ['photo','name','text','Cname','updated']
    search_fields = ['photo','name','text','Cname','updated']
    list_filter = ['photo','name','text','Cname','updated']
    style_fields = {'text': 'ueditor'}
    list_per_page = 10
    list_eitable = ['text']
    model_icon = 'fa fa-list'

class LabelAdmin(object):
    list_display = [ 'name', ]
    search_fields = [ 'name',  'updatetime']
    list_filter = [ 'name', 'updatetime']
    model_icon = 'fa fa-list'
class CommentsAdmin(object):
    list_display = ['name', 'email', 'body', 'created','post']
    search_fields = ['name', 'email', 'body', 'created','post']
    list_filter = ['name', 'email', 'body', 'created','post']
    model_icon = 'fa fa-cog fa-spin'
class AdminIMGAdmin(object):
    list_display = ['filename', 'img']
    search_fields = ['filename', 'img']

xadmin.site.register(Painting,PaintingAdmin)
xadmin.site.register(Label,LabelAdmin)
xadmin.site.register(Comments,CommentsAdmin)
xadmin.site.register(AdminIMG,AdminIMGAdmin)