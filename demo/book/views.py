
import os
from datetime import datetime

from django.shortcuts import render, reverse
from django.views import View
from book.models import BookInfo, HeroInfo
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.template import loader
import json


# Create your views here.


# class BookView(View):
#     def get(self, request):
#         """
#             获取图书数据
#         :param request:
#         :return:
#         """
#         # 1、查询图书
#         book = BookInfo.objects.get(id=1)
#         # 2、构建上下文
#         context = {
#             'btitle': book.btitle,
#             'bread': book.bread
#         }
#         # 模板渲染
#         html_str = render(request, 'index.html', context)
#         return html_str
#         # template=loader.get_template('index.html')
#         # html_str = template.render(context)
#         # # html_str=html_str.decode()
#         # file_path=os.path.join(settings.BASE_DIR,'static_files/index.html')
#         # with open(file_path,'w',encoding='utf-8') as f:
#         #     f.write(html_str)
#         # return HttpResponse('ok')
#         # 前后端分离返回json数据
#         # return JsonResponse(context)
#
#
# class HeroView(View):
#     def get(self, request, id, version):
#         """
#             获取英雄信息
#         :param request:
#         :return:
#         """
#         if version == '1.0':
#             her = HeroInfo.objects.get(id=id)
#             context = {
#                 'hname': her.hname,
#                 'hcomment': her.hcomment
#             }
#         elif version == '2.0':
#             her = HeroInfo.objects.get(pk=id)
#             context = {
#                 'hname': her.hname,
#                 'hgender': her.hgender
#             }
#         else:
#             context = {
#             }
#         # request.META['version']
#         return JsonResponse(context)

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
        # 2、返回图书数据
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bpub_date': book.bpub_date
            }
        )

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

