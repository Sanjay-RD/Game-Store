from django.db import models
from django.db.models.base import Model
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Game(models.Model):
    gameTitle = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    mainDescription = RichTextField()
    minimumRequirement = RichTextField(config_name="special")
    recommendedRequirement = RichTextField(config_name="special")
    photo_icon_small = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_trending = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.gameTitle
