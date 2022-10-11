from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from question_app import views

urlpatterns = [
    path('', views.api_root),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(),
         name='question-detail'),
    path('user/questions/', views.UserQuestionList.as_view(),
         name='user-question-list'),
    path('answers/', views.CreateAnswer.as_view(), name='answer-list'),
    path('answers/<int:pk>/', views.AnswerDetail.as_view(), name='answer-detail'),
    path('answers/<int:pk>/accept',
         views.AcceptAnswer.as_view(), name='answer-accept'),
    path('user/answers/', views.UserAnswerList.as_view(), name='user-answer-list'),
    path('favorites/', views.FavoriteList.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteDetail.as_view(),
         name='favorite-detail'),
    path('user/favorites/', views.UserFavoriteList.as_view(),
         name='user-Favorite-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
