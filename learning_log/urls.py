'''learning_log의 url 패턴 정의'''

from django.urls import path
from . import views

app_name = 'learning_log'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # Topic list
    path('topics/', views.topics, name='topics'),
    # Topic detail page
    path('topics/<int:topic_id>', views.topic, name='topic'),
]
