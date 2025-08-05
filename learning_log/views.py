from django.shortcuts import render

# Create your views here.
def index(requst):
      '''learning log homepage'''
      return render(requst, 
                    'learning_log/index.html')
      
      