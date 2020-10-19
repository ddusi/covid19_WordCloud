from django.urls import path

from . import views


app_name = 'covid'
urlpatterns = [
    path('', views.index, name='index'),
    path('News', views.News, name='News'),
    path('basic_information', views.basic_information, name='basic_information'),
    path('QnA', views.QnA, name='QnA'),
    path('new',views.new, name='new'),
    path('create',views.create, name='create'),
    path('Precautions', views.Precautions, name='Precautions'),
    path('<int:question_id>/', views.ques, name='ques'),
    path('<int:question_id>', views.answer, name='answer'),
]