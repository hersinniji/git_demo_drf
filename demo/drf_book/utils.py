# 完成分页两个步骤:
# 第一步,先自定义一个分页器
# 第二步,在视图中指定分页器
from rest_framework.pagination import PageNumberPagination


class PageNum(PageNumberPagination):
    """
        自定义分页器
    """
    page_size_query_param = 'page_size'  # 指定分页中每页展示数量参数
    max_page_size = 5  # 指定每页最大返回数量
