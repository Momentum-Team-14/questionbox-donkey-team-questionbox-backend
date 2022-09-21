from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Question
from rest_framework import generics
from .serializers import QuestionSerializer


# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'question_app': reverse('question-list', request=request, format=format)
    })
