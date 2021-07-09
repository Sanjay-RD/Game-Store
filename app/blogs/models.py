from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.


class Blog(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=200)
    blogImage = models.ImageField(upload_to='photos/%y/%m/%d/')
    blogTitle = models.CharField(max_length=200)
    blogDescription = RichTextField()
    published_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.blogTitle
