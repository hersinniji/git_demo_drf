# 完成分页两个步骤:
# 第一步,先自定义一个分页器
# 第二步,在视图中指定分页器
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
from django.db import DatabaseError


class PageNum(PageNumberPagination):
    """
        自定义分页器
    """
    page_size_query_param = 'page_size'  # 指定分页中每页展示数量参数
    max_page_size = 5  # 指定每页最大返回数量


# 处理关于数据库的异常
def exception_handler(exc, context):
    # 捕获drf异常,如果是默认异常,直接进行response.如果不是默认的异常(默认异常范围内),这里会返回一个None值给response
    response = drf_exception_handler(exc, context)

    # 如果不是默认异常,看这个异常是什么
    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError):
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response