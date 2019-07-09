from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book.models import BookInfo
from drf_book.serializer import BookSerializer


# 对同一张表进行增删改查多个操作时可以用视图集
class BooksModelViewSet(ModelViewSet):

    # ① 指定查询集属性
    queryset = BookInfo.objects.all()
    # ② 指定序列化器
    serializer_class = BookSerializer

    """自定义查询"""
    # todo 只用视图集时,如果自定义了一个方法,那么需要把这个方法名定义在请求路径当中
    # 获取最后一本图书的数据
    def last_book(self, request):
        book = BookInfo.objects.latest('id')
        ser = self.get_serializer(book)
        return Response(ser.data)

    """
    REST framework 提供了Parser解析器，在接收到请求后会自动根据Content-Type指明的请求数据类型（如JSON、表单等）
    将请求数据进行parse解析，解析为类字典对象保存到Request对象中。
    Request对象的数据是自动根据前端发送数据的格式进行解析之后的结果。
    无论前端发送的哪种格式的数据，我们都可以以统一的方式读取数据。
    request常用属性:
    1）.data
    request.data 返回解析之后的请求体数据。类似于Django中标准的request.POST和 request.FILES属性
    但提供如下特性：
        ①包含了解析之后的文件和非文件数据
        ②包含了对POST、PUT、PATCH请求方式解析后的数据
        ③利用了REST framework的parsers解析器，不仅支持表单类型数据，也支持JSON数据
    2）.query_params
    request.query_params与Django标准的request.GET相同，只是更换了更正确的名称而已。
    """

    # 按照书名查询数据
    def find(self, request):
        data = request.query_params
        btitle = data.get('btitle')
        book = BookInfo.objects.get(btitle=btitle)
        ser = self.get_serializer(book)
        return Response(ser.data)
