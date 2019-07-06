"""
这里自定义序列化器时需要继承drf框架自带的模型
"""


from rest_framework import serializers


# 自定义序列化器,创建序列化器类
class BookSerializer(serializers.Serializer):

    """
        图书序列化器
    """
    # 1.定义字段
    id = serializers.IntegerField()
    btitle = serializers.CharField()
    bpub_date = serializers.DateField(default="1999-10-10")
    bread = serializers.IntegerField(min_value=1, max_value=200)
    is_delete = serializers.BooleanField(required=False)
    # h_name = serializers.BooleanField(write_only=True)


# 自定义序列化器
class HeroSerializer(serializers.Serializer):
    """
        英雄序列化器
    """
    # 1.定义字段
