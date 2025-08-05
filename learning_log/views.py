from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

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
            
      
def new_topic(request):
      '''add new topic'''
      if request.method != 'POST':
            # 빈 폼을 만든다
            form = TopicForm()
      else:
            # POST 데이터를 받았으므로 이를 처리한다
            form = TopicForm(data=request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('learning_log:topics')
      '''
      # 아래의 코드가 실행되는 경우:
      1. GET 요청: 처음 페이지 방문 → 빈 폼 보여줌
      2. POST 요청이지만 데이터가 invalid: 에러 메시지와 함께 폼 다시 보여줌     
      '''
      context = {'form': form}
      return render(request,
                    'learning_log/new_topic.html',
                    context)
      
      
def new_entry(request, topic_id):
      '''특정 topic에 대한 entry 추가하기'''
      topic = Topic.objects.get(id=topic_id)
      
      if request.method != 'POST':
            # POST 메소드가 아닌 경우에는 빈 폼을 만든다
            form = EntryForm()
      else:
            # POST 데이터를 받은 경우 처리하기
            form = EntryForm(data=request.POST)
            if form.is_valid():
                  new_entry = form.save(commit=False)
                  new_entry.topic = topic
                  new_entry.save()
                  return redirect('learning_log:topic', topic_id=topic_id)
      
      # 빈 폼 or invalid 폼을 표시한다
      context = {'topic': topic, 'form': form}
      return render(request,
                    'learning_log/new_entry.html',
                    context)
                  