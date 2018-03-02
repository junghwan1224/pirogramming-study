from django.urls import path

from . import views

app_name = 'core'
# 없어도 돌아가지만, 후에 namespace 등을 못주기 때문에 지정해준다.

urlpatterns = [
    ########################### 2017. 1. 17 ####################
    path('article/<int:pk>', views.blog_detail, name='blog_detail'), # 2018. 1. 17 동적으로 렌더링
    path('article/', views.blog_list, name='blog_list'),
    path('article/create/', views.blog_create, name='blog_create'),
    path('<int:pk>/update/', views.blog_update, name='blog_update'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('<int:pk>/like/', views.blog_like, name='blog_like'),
    path('<int:pk>/comment_like/', views.comment_like, name='comment_like'),
    path('tag/<int:tag_pk>', views.blog_list, name='article_list_by_tag'),
    ############################################################
    path('1/', views.one_func),
    path('2/', views.two_func),
    path('<int:pk>/', views.first_dynamic),
    path('cap_str/<str:url_path_str>/', views.capture_string),
    path('nav1/', views.nav1_test),
    path('nav2/', views.nav2_test),
]