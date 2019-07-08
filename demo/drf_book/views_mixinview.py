from rest_framework.response import Response

from book.models import BookInfo
from drf_book.serializer import BookSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView

"""
五个扩展类
"""


class BooksAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    获取所有图书和保存图书
    """
    # ① 指定查询集属性
    queryset = BookInfo.objects.all()
    # ② 指定序列化器
    serializer_class = BookSerializer

    def get(self, request):
        """
        获取所有图书
        :param request:
        :return:
        """
        return self.list(request)

    # rest_framework.mixins里面写的ListModelMixin类中的list函数:
    """
        def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
    
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
    
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
    """

    def post(self, request):
        """
        保存图书
        :param request:
        :return:
        """
        return self.create(request)


class BookAPIView(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    """
        获取单一图书数据
        更新图书
        删除图书
    """

    # ① 指定查询集属性
    queryset = BookInfo.objects.all()
    # ② 指定序列化器
    serializer_class = BookSerializer

    def get(self, request, pk):
        """
        获取单一图书数据
        :param request:
        :param pk:
        :return:
        """
        # RetrieveModelMixin类中 retrieve 函数步骤:
        # 一:获取对象;
        # 二:调用序列化器;
        # 三:序列化返回
        return self.retrieve(request)

    def put(self, request, pk):
        """
        更新图书信息
        :param request:
        :param pk:
        :return:
        """
        # 1.获取要保存的图书数据
        return self.update(request)

    def delete(self, request, pk):
        """
        删除图书
        :param request:
        :param pk:
        :return:
        """
        return self.destroy(request)

