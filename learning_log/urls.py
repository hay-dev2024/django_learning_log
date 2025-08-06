'''learning_log의 url 패턴 정의'''

from django.urls import path
from . import views

app_name = 'learning_log'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # Topic list page
    path('topics/', views.topics, name='topics'),
    # Topic detail page
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # add New Topic page
    path('new_topic/', views.new_topic, name='new_topic'),
    # add New Entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name="new_entry"),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
