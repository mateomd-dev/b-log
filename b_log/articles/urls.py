from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from articles import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name='article-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)

