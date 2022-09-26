from rest_framework import serializers
from .models import Answer, Favorite, Question


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Question
        fields = ('pk', 'user', 'question_title',
                  'question_field', 'date_created')


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Answer
        fields = ('pk', 'user', 'question',
                  'answer_field', 'date_answered', 'accepted')


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Favorite
        fields = ('pk', 'user', 'question')
