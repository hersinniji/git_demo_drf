from django.conf.urls import url
from django.contrib import admin
from . import views, views_apiview, views_genericapiview, views_mixinview
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
    url(r'^drf_books/$', views_mixinview.BooksAPIView.as_view()),
    url(r'^drf_books/(?P<pk>\d+)/$', views_mixinview.BookAPIView.as_view()),
]
