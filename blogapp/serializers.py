from rest_framework import serializers
from .models import BlogCategory, BlogPost, BlogComments

#Her bir class icinde gecerli olacak seyler icin bir adet FixSerializer olusturuyorum.

#--------------------------FixSerializer----------------------------#
class FixSerializer(serializers.ModelSerializer) :

    class Meta :
        exclude=[
            'created_date',
            'updated_date'
        ]


#--------------------------Serializers----------------------------#
class BlogCommentSerializer(FixSerializer) :
    blog_post = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta(FixSerializer.Meta) :
        model = BlogComments


class BlogPostSerializer(FixSerializer) :
    # blog_category_id = serializers.IntegerField()
    blog_category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    blog_comment = BlogCommentSerializer(read_only=True, many=True)
    class Meta(FixSerializer.Meta) :
        model = BlogPost


class BlogCategorySerializer(FixSerializer) :
    user_id = serializers.IntegerField(read_only=True)
    user = serializers.StringRelatedField()

    class Meta(FixSerializer.Meta) :
        model = BlogCategory
