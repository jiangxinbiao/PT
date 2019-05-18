# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import UserProfile,EmailVerifyRecode

class UserSerializer(serializers.ModelSerializer):
    #让字段显示使用中文别名
    user_type_name = serializers.CharField(source="get_user_type_display")
    gender_name = serializers.CharField(source="get_gender_display")
    class Meta:
        model = UserProfile
        fields = ('username','user_type_name','gender_name')#user_type_name，gender_name，然后将修改后的字段名加入到需要序列化的字段列表中
        # depth = 1#深度搜索更多的关联数据库 如 外键 多对多 一对一的表


class EmailVerifyRecodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerifyRecode
        fields = ('email',)

