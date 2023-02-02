from rest_framework import serializers
from .models import BlogCategory, BlogPost, BlogComments

#Her bir class icinde gecerli olacak seyler icin bir adet FixSerializer olusturuyorum.

#--------------------------FixSerializer----------------------------#
class FixSerializer(serializers.ModelSerializer) :

    class Meta :
        exclude=[]


#--------------------------Serializers----------------------------#
class BlogCommentSerializer(FixSerializer) :

    class Meta(FixSerializer.Meta) :
        model = BlogComments


class BlogPostSerializer(FixSerializer) :

    class Meta(FixSerializer.Meta) :
        model = BlogPost


class BlogCategorySerializer(FixSerializer) :

    class Meta(FixSerializer.Meta) :
        model = BlogCategory
