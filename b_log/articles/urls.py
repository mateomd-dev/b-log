from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from articles import views as article_views

urlpatterns = [
    path('articles/', article_views.ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>', article_views.ArticleDetail.as_view(), name='article-detail'),
    path('articles/<int:pk>/', include('comments.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

