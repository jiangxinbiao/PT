from rest_framework import serializers
from Paintings.models import Painting,Label,Comments
from django.forms import ValidationError

"""设置禁用敏感字符元组应用到钩子函数中"""
A = ('a','b','c','d','e',)


class PaintingSerializer(serializers.ModelSerializer):
    # def validate_字段(self, validated_value):
    #     raise ValidationError(detail='xxxxxx')
    #     return validated_value
    text = serializers.CharField(error_messages={'required':'说明不能为空'})
    class Meta:
        model = Painting
        fields = ('name','Ph','Pt','text') #序列化需要的数据     'photo','url_height','url_width','Ph','Pt',
        # depth = 1


    """钩子函数做数据验证"""
    def validate_name(self, value):#局部钩子函数
        if value.startswith(A):
            raise ValidationError('不能以敏感字符開頭')
        # if value.startswith(''):
        #     raise ValidationError('不能为空')
        else:
            return value
    def validate(self, value): # 全局钩子函數
        if len(value['name']) < 1 :
            raise ValidationError('名稱不能太短')
        if value['name'] == value['text']:
            raise ValidationError('不能雷同')
        else:
            return value


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    Painting = serializers.HyperlinkedIdentityField(view_name="pt",lookup_field="post_id",lookup_url_kwarg="pk")#在响应数据中携带url，可查询特定外键的详细信息,lookup_url_kwarg="pk",
    class Meta:
        model = Comments
        fields = ('name','body','Painting')
        depth = 0# 深度

