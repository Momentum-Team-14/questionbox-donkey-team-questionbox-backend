from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from question_app import views

urlpatterns = [
    path('question_app/', views.QuestionList.as_view(), name='question-list'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
