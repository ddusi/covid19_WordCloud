from django.urls import path

from .views import *

app_name = 'covid'
urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('covid-info/', views.covid_info, name='covid-info'),
    # path('qna/', views.qna, name='qna'),
    # path('new-question/',views.new_question, name='new_question'),
    # path('<int:question_id>/', views.question_read, name='question'),
    # path('<int:question_id>/', views.answer, name='answer'),
    path('precautions/', QuestionCRUDView.as_view(), name='precautions'),
]