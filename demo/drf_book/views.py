import json

from django.http import JsonResponse


# Create your views here.
from django.views import View

from book.models import BookInfo
from drf_book.serializer import BookSerializer

"""
drf框架中的serializer序列化器的使用
序列化器可以帮我们完成序列化的反序列化的所有功能和过程
"""


# 继承View也可以使用drf框架的序列化器
# 这里使用View,不继承drf的类视图框架也可以完成,因为drf框架就是基于django开发的
class BooksView(View):
    """
        获取所有图书和保存图书
    """

    def get(self, request):
        """
            获取所有图书
        :param request:
        :return:
        """
        # 1、查询图书表获取所有图书对象
        books = BookInfo.objects.all()

        """
        # 2、提取所有对象的字段内容
        book_list = []
        for book in books:
            data = {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bpub_date': book.bpub_date
            }
            book_list.append(data)
        # 3、返回所有对象字段内容
        return JsonResponse({'book_list': book_list})
        """

        # 1.初始化 生成序列化器对象,因为这里books是多个对象,所以要加many=True
        ser = BookSerializer(books, many=True)
        # 2.使用序列化器对象的data方法获取序列化后的结果
        data = ser.data
        # print(type(data))
        # print(data)
        return JsonResponse({'book_list': data})

    def post(self, request):
        """
            保存图书
        :param request:
        :return:
        """
        # 1、获取保存的图书数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证图书数据字段
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')
        if btitle is None or bpub_date is None:
            return JsonResponse({'error': '缺少必要数据'})
        # 3、保存图书
        book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)
        # 4、返回保存后的图书数据

        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bpub_date': book.bpub_date
            }
        )


class BookView(View):
    """
        获取单一图书数据
        更新图书
        删除图书
    """

    def get(self, request, pk):
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
            return JsonResponse({'error': '错误的id值'})

        """
         # 2、返回图书数据
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bpub_date': book.bpub_date
            }
        )
        """

        ser = BookSerializer(book)
        print(type(ser.data))
        return JsonResponse({'book': ser.data})

    def put(self, request, pk):
        """
         更新图书信息
        :param request:
        :param pk:
        :return:
        """
        # 1.判断书籍是否存在
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'error': '书籍不存在'})
        json_dict = json.loads(request.body.decode())

        # 方法一:
        # book.btitle = json_dict.get('btitle')
        # book.bpub_date = datetime.strptime(json_dict.get('bpub_date'), '%Y-%m-%d').date()
        # book.save()
        # 方法二:
        # todo 此处可以通过拆包的形式进行赋值,减少代码量.另外注意更新操作是无返回值的
        # 因为字典类型数据 'btitle': 'python' 经**转换后就会转换为'btitle'='python'的格式
        BookInfo.objects.filter(pk=pk).update(**json_dict)
        book = BookInfo.objects.get(pk=pk)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        })

    def delete(self, request, pk):
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
            return JsonResponse({'error': '书籍不存在'})

        # 1.物理删除
        # book.delete()
        # 2.逻辑删除
        book.is_delete = True
        book.save()

        return JsonResponse({})