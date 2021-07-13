from django.db import models

# Create your models here.
class Review(models.Model):
    user_id = models.IntegerField()
    user_name=models.CharField(max_length=200)
    rating = models.IntegerField()
    comments = models.TextField(max_length=200)

    def __str__(self):
        return self.user_name