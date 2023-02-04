from django.db import models
from django.contrib.auth.models import User

class Account(User) :
    image = models.ImageField(blank=True, null=True, upload_to="blogapp_user/images/")
