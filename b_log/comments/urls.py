from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from comments import views

urlpatterns = [
        path('comments/', views.CommentList.as_view(), name='comment-list')
]


