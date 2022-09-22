from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='users', blank=True, null=True)

    pass

    def __str__(self):
        return self.username


class Question(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="question")
    question_title = models.CharField(max_length=250, blank=True, default='')
    question_field = models.TextField(max_length=10000, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_field


class Answer(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="answer")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer', null=True, blank=True)
    answer_field = models.TextField(max_length=10000, blank=True, default='')
    date_answered = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_field


class Favorite(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="favorite")
