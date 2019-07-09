from django.conf.urls import url
from rest_framework.routers import SimpleRouter, DefaultRouter

from drf_book import view_viewset
from . import views_modelviewset
urlpatterns = [
    # url(r'^book/$',views.BookView.as_view() ),
    # url(r'^hero/(?P<id>\d+)/$',views.HeroView.as_view() ),
    # 获取所有和保存图书
    # url(r'^drf_books/$', views.BooksView.as_view()),
    # url(r'^drf_books/(?P<pk>\d+)/$', views.BookView.as_view()),
    # APIView使用
    # url(r'^drf_books/$', views_apiview.BooksAPIView.as_view()),
    # url(r'^drf_books/(?P<pk>\d+)/$', views_apiview.BookAPIView.as_view()),
    # GenericAPIView使用
    # url(r'^drf_books/$', views_genericapiview.BooksAPIView.as_view()),
    # url(r'^drf_books/(?P<pk>\d+)/$', views_genericapiview.BookAPIView.as_view()),
    # 拓展类的使用
    # url(r'^drf_books/$', views_mixinview.BooksAPIView.as_view()),
    # url(r'^drf_books/(?P<pk>\d+)/$', views_mixinview.BookAPIView.as_view()),
    # 拓展类子类的使用
    # url(r'^drf_books/$', views_mixinchildview.BooksAPIView.as_view()),
    # url(r'^drf_books/(?P<pk>\d+)/$', views_mixinchildview.BookAPIView.as_view()),
    # viewset视图集使用
    url(r'^viewset_books/$', view_viewset.BooksViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^viewset_books/(?P<pk>\d+)/$', view_viewset.BookViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    # genericviewset视图集使用
    # url(r'^genericviewset_books/$', views_genericviewset.BooksGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^genericviewset_books/(?P<pk>\d+)/$', views_genericviewset.BookGenericViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    # modelviewset视图集使用
    # url(r'^modelviewset_books/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^modelviewset_books/(?P<pk>\d+)/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    # modelviewset视图集使用(增加功能函数)
    # url(r'^modelviewset_books/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^modelviewset_books/(?P<pk>\d+)/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    # url(r'^modelviewset_books/last_book/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'last_book'})),
    # url(r'^modelviewset_books/find/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'find'})),

]

# todo 如果想用自动生成路由的方法时, 类视图必须继承自视图集viewset
# 自动生成路由方法: 生成路由类对象
# 自定义的方法要想自动生成路由,方法名上面写 @action(methods=['get/......'], detail=True/False)
# router = SimpleRouter()
# router.register('modelviewset_books', views_modelviewset.BooksModelViewSet, base_name='book')
# print(router.urls)
# urlpatterns += router.urls

# DefaultRouter继承自SimpleRouter,使用方法完全一致,区别就是是否生成首页匹配
# todo DefaultRouter会进行首页的匹配,自动生成首页的路由信息
router = DefaultRouter()
router.register('modelviewset_books', views_modelviewset.BooksModelViewSet, base_name='book')
# print(router.urls)
urlpatterns += router.urls
