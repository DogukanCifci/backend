from django.urls import path,include
from .views import BlogPostView, BlogCategoryView, BlogCommentsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', BlogCategoryView)
router.register('posts', BlogPostView)
router.register('comments', BlogCommentsView)

urlpatterns = [
path('', include(router.urls))
]
