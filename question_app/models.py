from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='users', blank=True, null=True)

    pass

    def __str__(self):
        return self.username


class Question(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="questions")
    question_title = models.CharField(max_length=250, blank=True, default='')
    question_field = models.TextField(max_length=10000, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', null=True, blank=True)
    answer_field = models.TextField(max_length=10000, blank=True, default='')
    date_answered = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_field


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="favorites", null=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="favorites")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'question'], name='unique_for_question_and_user'
            )
        ]
