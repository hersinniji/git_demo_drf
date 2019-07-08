from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from book.models import BookInfo
from drf_book.serializer import BookSerializer


"""
如果继承自rest_framework框架的APIViews的话,使用浏览器访问会有可视化内容,但继承django自带的View不会有可视化界面

APIView和View在业务逻辑上没有变化,但使用方法换了一下: 获取数据的形式发生了变化,响应类也发生了变化,
"""


class BooksAPIView(GenericAPIView):
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
        # 1、查询图书表获取所有图书对象 self.get_queryset()获取queryset属性中的所有数据
        books = self.get_queryset()
        # 2.初始化 生成序列化器对象 self.get_serializer获取serializer_class所指定的
        # 序列化器进行初始化操作
        ser = self.get_serializer(books, many=True)
        # 3.使用序列化器对象的data方法获取序列化后的结果,并返回
        return Response({'book_list': ser.data})

    def post(self, request):
        """
        保存图书
        :param request:
        :return:
        """
        # 1.获取保存的图书数据
        data = request.data
        # 2.通过反序列化获取前端提交的json数据
        ser = self.get_serializer(data=data)
        # 3.验证图书字段,验证不通过直接返回错误信息
        ser.is_valid(raise_exception=True)
        # 4.调用序列化器中封装的保存方法create
        ser.save()
        # 5.序列化返回操作,data方法即是获取序列化后的字典数据
        return Response(ser.data)


class BookAPIView(GenericAPIView):
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
        # 1、根据pk值查询图书对象
        try:
            # self.get_object() 从 queryset中获取当前pk所对应的数据对象
            book = self.get_object()
        except:
            return Response({'error': '错误的id值'})
        ser = self.get_serializer(book)
        return Response({'book': ser.data})

    def put(self, request, pk):
        """
        更新图书信息
        :param request:
        :param pk:
        :return:
        """
        # 1.获取要保存的图书数据
        data = request.data
        try:
            book = self.get_object()
        except:
            return Response({'error': '书籍不存在'})
        # 2.通过反序列化验证图书字段
        ser = self.get_serializer(book, data=data)
        ser.is_valid(raise_exception=True)
        # 3.调用序列化器中封装的update更新图书方法
        ser.save()
        # 4.序列化返回操作(data即是序列化后的字典数据)
        return Response(ser.data)

    def delete(self, request, pk):
        """
        删除图书
        :param request:
        :param pk:
        :return:
        """
        # 1.判断书籍是否存在
        try:
            book = self.get_object()
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'})
        # 2.逻辑删除
        book.is_delete = True
        book.save()

        return Response({})
