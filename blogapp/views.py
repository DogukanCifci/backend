from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .serializers import BlogCategorySerializer,BlogPostSerializer, BlogCommentSerializer
from .models import BlogCategory,BlogPost,BlogComments


class BlogCategoryView(ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogPostView(ModelViewSet) :
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogCommentsView(ModelViewSet):
    queryset = BlogComments.objects.all()
    serializer_class = BlogCommentSerializer
