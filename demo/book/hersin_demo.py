import json

from django.http import JsonResponse
from django.views import View

from book.models import BookInfo


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
        # 1.查询图书表获取所有图书对象
        books = BookInfo.objects.all()
        # 2.提取所有对象的字段内容
        book_list = []
        for book in books:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bpub_date': book.bpub_date
            })
        # 3.返回所有字段内容
        return JsonResponse({'book_list': book_list})

    def post(self, request):

        """
            保存图书
        :param request:
        :return:
        """
        # 1.接收保存字段数据
        json_dict = json.loads(request.body.decode())
        btitle = json_dict.get('btitle')
        pub_date = json_dict.get('bpub_date')
        # 2.验证数据
        if not all([btitle, pub_date]):
            return JsonResponse({'error': '缺少必要参数'})
        # 3.保存图书信息
        book = BookInfo.objects.create(btitle=btitle, bpub_date=pub_date)
        # 4.返回响应(json字符串)
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bread': book.bread,
            'bpub_date': book.bpub_date

        })


class BookView(View):

    def get(self, request, pk):

        """
            获取单一图书
        :param request:
        :param pk:
        :return:
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as e:
            return JsonResponse({'error': '此书无记录'})
        return JsonResponse({'btitle'})


