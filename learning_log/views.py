from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(requst):
      '''learning log homepage'''
      return render(requst, 
                    'learning_log/index.html')
      
      
def topics(request):
      '''topics list'''
      topics = Topic.objects.order_by('date_added')
      context = {'topics': topics}
      return render(request,
                    'learning_log/topics.html',
                    context)
      
      
def topic(request, topic_id):
      '''topic detail'''
      topic = Topic.objects.get(id=topic_id)
      entries = topic.entry_set.order_by('-date_added')
      context = {'topic': topic, 'entries': entries}
      return render(request, 
                    'learning_log/topic.html',
                    context)
            
      