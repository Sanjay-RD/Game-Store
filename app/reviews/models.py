from django.db import models
from datetime import datetime

# Create your models here.
class Review(models.Model):
    blog_id = models.IntegerField()
    user_id = models.IntegerField()
    user_name=models.CharField(max_length=200)
    rating = models.IntegerField()
    comments = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user_name