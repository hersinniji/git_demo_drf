from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    # url(r'^book/$',views.BookView.as_view() ),
    # url(r'^hero/(?P<id>\d+)/$',views.HeroView.as_view() ),
    # 获取所有和保存图书
    url(r'^drf_books/$', views.BooksView.as_view()),
    url(r'^drf_books/(?P<pk>\d+)/$', views.BookView.as_view()),

]
