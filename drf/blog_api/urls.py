from django.urls import path

from .views import PostList, PostDetail, PostListDetailFilter

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listcreate'),
    path('<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
]
