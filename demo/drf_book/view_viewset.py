from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from book.models import BookInfo
from drf_book.serializer import BookSerializer


"""
如果继承自rest_framework框架的APIViews的话,使用浏览器访问会有可视化内容,但继承django自带的View不会有可视化界面

APIView和View在业务逻辑上没有变化,但使用方法换了一下: 获取数据的形式发生了变化,响应类也发生了变化,
"""


class BooksViewSet(ViewSet):
    """
    获取所有图书和保存图书
    """
    def list(self, request):
        """
        获取所有图书
        :param request:
        :return:
        """
        # 1、查询图书表获取所有图书对象
        books = BookInfo.objects.all()
        # 2.初始化 生成序列化器对象,因为这里books是多个对象,所以要加many=True
        ser = BookSerializer(books, many=True)
        # 3.使用序列化器对象的data方法获取序列化后的结果,并返回
        return Response({'book_list': ser.data})

    def create(self, request):
        """
        保存图书
        :param request:
        :return:
        """
        # 1.获取保存的图书数据
        data = request.data
        # 2.通过反序列化获取前端提交的json数据
        ser = BookSerializer(data=data)
        # 3.验证图书字段,验证不通过直接返回错误信息
        ser.is_valid(raise_exception=True)
        # 4.调用序列化器中封装的保存方法create
        ser.save()
        # 5.序列化返回操作,data方法即是获取序列化后的字典数据
        return Response(ser.data)


class BookViewSet(ViewSet):
    """
        获取单一图书数据
        更新图书
        删除图书
    """
    def retrieve(self, request, pk):
        """
        获取单一图书数据
        :param request:
        :param pk:
        :return:
        """
        # 1、根据pk值查询图书对象
        try:
            book=BookInfo.objects.get(id=pk)
        except:
            return Response({'error': '错误的id值'})
        ser = BookSerializer(book)
        return Response({'book': ser.data})

    def update(self, request, pk):
        """
        更新图书信息
        :param request:
        :param pk:
        :return:
        """
        # 1.获取要保存的图书数据
        data = request.data
        try:
            book = BookInfo.objects.get(pk=pk)
        except:
            return Response({'error': '书籍不存在'})
        # 2.通过反序列化验证图书字段
        ser = BookSerializer(book, data=data)
        ser.is_valid(raise_exception=True)
        # 3.调用序列化器中封装的update更新图书方法
        ser.save()
        # 4.序列化返回操作(data即是序列化后的字典数据)
        return Response(ser.data)

    def destroy(self, request, pk):
        """
        删除图书
        :param request:
        :param pk:
        :return:
        """
        # 1.判断书籍是否存在
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return Response({'error': '书籍不存在'})
        # 2.逻辑删除
        book.is_delete = True
        book.save()

        return Response({})
