from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')
    
    def popular(self):
        return self.order_by('-rating')
    
    
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, 
        null=False, 
        blank=False, 
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        null=False, 
        blank=False,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        null=False, 
        blank=False,
        on_delete=models.CASCADE
    )
