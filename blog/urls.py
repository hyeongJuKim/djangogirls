from django.conf.urls import url
from . import views

urlpatterns = [

	# 블로그 목록
    url(r'^$', views.post_list, name='post_list'),

    # 블로그 상세화면
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

    # 블로그 입력 
    url(r'^post/new/$', views.post_new, name='post_new'),

    # 블로그 수정
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]