from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    img = models.ImageField(upload_to = 'pics/', blank=True, null=True)
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(default = timezone.now)



    def __str__(self):
        return self.title





class AddComment(models.Model):
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    comment = models.TextField()
    
    

    