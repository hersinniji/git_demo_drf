from django.conf.urls import url
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
    # url(r'^viewset_books/$', view_viewset.BooksViewSet.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^viewset_books/(?P<pk>\d+)/$', view_viewset.BookViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    # genericviewset视图集使用
    # url(r'^genericviewset_books/$', views_genericviewset.BooksGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^genericviewset_books/(?P<pk>\d+)/$', views_genericviewset.BookGenericViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    # modelviewset视图集使用
    url(r'^modelviewset_books/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^modelviewset_books/(?P<pk>\d+)/$', views_modelviewset.BooksModelViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]
