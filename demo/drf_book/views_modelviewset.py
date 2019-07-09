from rest_framework.viewsets import ModelViewSet

from book.models import BookInfo
from drf_book.serializer import BookSerializer


# 对同一张表进行增删改查多个操作时可以用视图集
class BooksModelViewSet(ModelViewSet):

    # ① 指定查询集属性
    queryset = BookInfo.objects.all()
    # ② 指定序列化器
    serializer_class = BookSerializer
