from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Answer, Question
from rest_framework import generics, filters
from .serializers import QuestionSerializer, AnswerSerializer


# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['date_created']
    search_fields = ['question_title', 'question_field']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_answered']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        question=serializer.validated_data.get('question'))


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'extra-pointers': reverse('question-list', request=request, format=format),
        'answers': reverse('answer-list', request=request, format=format),
    })
