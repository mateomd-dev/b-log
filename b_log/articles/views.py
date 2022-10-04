from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from articles.models import Article
from articles.serializers import ArticleListSerializer, ArticleDetailSerializer
from articles.permissions import IsOwnerOrReadOnly


class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleDetailSerializer

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
