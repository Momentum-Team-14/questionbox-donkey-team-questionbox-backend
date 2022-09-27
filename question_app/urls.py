from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from question_app import views

urlpatterns = [
    path('', views.api_root),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(),
         name='question-detail'),
    path('answers/', views.AnswerList.as_view(), name='answer-list'),
    path('answers/<int:pk>/', views.AnswerDetail.as_view(), name='answer-detail'),
    path('answers/<int:pk>/accept',
         views.AcceptAnswer.as_view(), name='answer-accept'),
    path('favorite/', views.FavoriteList.as_view(), name='favorite-list'),
    path('favorite/<int:pk>/', views.FavoriteDetail.as_view(),
         name='favorite-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
