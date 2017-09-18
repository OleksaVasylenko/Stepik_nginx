from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(
        User, 
        null=False, 
        blank=False, 
        on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(User, related_name='likes_set')


class Anwser(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        null=False, 
        blank=False,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        null=False, 
        blank=False,
        on_delete=models.CASCADE
    )
