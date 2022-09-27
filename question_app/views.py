from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Answer, Question, Favorite
from rest_framework import generics, filters, serializers
from .serializers import QuestionSerializer, AnswerSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.core.exceptions import PermissionDenied


# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['date_created']
    search_fields = ['question_title', 'question_field']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionDetail(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class UserQuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Question.objects.filter(user=self.request.user.pk)
        return queryset


class AnswerList(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_answered']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        question=serializer.validated_data.get('question'))


class AnswerDetail(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


class UserAnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Answer.objects.filter(user=self.request.user.pk)
        return queryset


class AcceptAnswer(generics.UpdateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_object(self):

        answer = super().get_object()

        if self.request.user != answer.question.user:
            raise PermissionDenied()
            # I don't really need to do this check because I have set the queryset
            # to _only_ the recipes belonging to the authenticated user
            # but it makes this extra explicit
        return answer

    def perform_update(self, serializer):
        serializer.save(accepted=True)


class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user,
                            question=serializer.validated_data.get('question'))
        except IntegrityError as error:
            raise serializers.ValidationError({"error": error})


class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]


class UserFavoriteList(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user.pk)
        return queryset


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'extra-pointers': reverse('question-list', request=request, format=format),
        'answers': reverse('answer-list', request=request, format=format),
        'favorite': reverse('favorite-list', request=request, format=format),
    })
