"""拓展类子类"""
from book.models import BookInfo
from drf_book.serializer import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

"""
五个扩展类
"""


class BooksAPIView(ListCreateAPIView):
    """
    获取所有图书和保存图书
    """
    # ① 指定查询集属性
    queryset = BookInfo.objects.all()
    # ② 指定序列化器
    serializer_class = BookSerializer


class BookAPIView(RetrieveUpdateDestroyAPIView):
    """
        获取单一图书数据
        更新图书
        删除图书
    """

    # ① 指定查询集属性
    queryset = BookInfo.objects.all()
    # ② 指定序列化器
    serializer_class = BookSerializer


