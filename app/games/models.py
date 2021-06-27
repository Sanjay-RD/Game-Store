from django.db import models
from django.db.models.base import Model
from datetime import datetime

# Create your models here.


class Game(models.Model):
    gameTitle = models.CharField(max_length=200)
    mainDescription = models.TextField()
    descriptionListOne = models.TextField(blank=True)
    descriptionListTwo = models.TextField(blank=True)
    descriptionListThree = models.TextField(blank=True)
    descriptionListFour = models.TextField(blank=True)
    minimumListOne = models.TextField()
    minimumListTwo = models.TextField()
    minimumListThree = models.TextField()
    minimumListFour = models.TextField()
    minimumListFive = models.TextField()
    recommendedListOne = models.TextField()
    recommendedListTwo = models.TextField()
    recommendedListThree = models.TextField()
    recommendedListFour = models.TextField()
    recommendedListFive = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_trending = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.gameTitle
