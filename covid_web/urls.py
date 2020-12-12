from django.urls import path

from .views.question_crud_view import QuestionCRUDView
from .views.views import home, covid_info, news
from .views.status_view import status

app_name = 'covid'
urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('covid-info/', covid_info, name='covid-info'),
    # path('qna/', views.qna, name='qna'),
    # path('new-question/',views.new_question, name='new_question'),
    # path('<int:question_id>/', views.question_read, name='question'),
    # path('<int:question_id>/', views.answer, name='answer'),
    path('precautions/', QuestionCRUDView.as_view(), name='precautions'),
    path('status/', status, name='status'),
]