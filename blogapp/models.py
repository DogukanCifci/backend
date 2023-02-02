from django.db import models
from django.contrib.auth.models import User

#Her bir class icinde gecerli olacak seyler icin bi FixModel olusturuyorum.

#--------------------------FIXMODELS----------------------------#

class FixModels(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta : 
        abstract = True #---->Bunu DB'de tablo olusturmamasi icin yaptik. Cünkü bunun icin ayri bir table olusturmasini istemiyorum.

#--------------------------MODELS----------------------------#
STATUS = (
    (0 , "Draft"),
    (1, "Publish")
)

class BlogCategory(FixModels):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta :
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BlogPost(FixModels) :
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.IntegerField(choices=STATUS,default=0)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128, default="")
    content = models.TextField()
    viewed = models.IntegerField(default=0, editable=False) #editable=False ise databasede gözükmez. Yani kullanici degistiremez. Bizim yazdigimiz fonksiyona göre arka planda kendini yenileyecek.
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self) :
        return f'{self.author} - {self.title}'

    class Meta : 
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_date']
    

class BlogComments(FixModels) :
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="blog_comment")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=64)
    comments = models.TextField()

    def __str__(self) :
        return f'{self.blog_post} - {self.title}'

    class Meta : 
        verbose_name = "Comment"
        verbose_name_plural = "Comments"