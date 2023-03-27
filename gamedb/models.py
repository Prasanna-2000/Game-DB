from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ManyToManyField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


# class Platform(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.name}"


class Info(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    dev = models.CharField(max_length=50)
    release_date = models.DateField()
    # platform = models.ManyToManyField(Platform)
    platform = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50)
    video = EmbedVideoField(null=True)

    def __str__(self):
        return f"{self.game}"


class Requirement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    cpu = models.CharField(max_length=150)
    graphics = models.CharField(max_length=150)
    directx = models.CharField(max_length=50, null=True)
    storage = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.game}"


class Detail(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    resolution = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)
    rtx_support = models.BooleanField()
    game_engine = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.game}"


class Rating(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    graphics = models.IntegerField()
    story_line = models.IntegerField()
    character = models.IntegerField()
    difficulty = models.IntegerField()
    steam = models.FloatField( default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    ign = models.FloatField( default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f"{self.game}"


