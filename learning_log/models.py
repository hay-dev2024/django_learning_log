from django.db import models

# Create your models here.
class Topic(models.Model):
      '''user가 배우는 주제'''
      text = models.CharField(max_length=200)
      date_added = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            '''model의 문자열 표현을 반환'''
            return self.text
      

class Entry(models.Model):
      '''Topic에 대해 배운 내용'''
      topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
      text = models.TextField()
      date_added = models.DateTimeField(auto_now_add=True)
      
      class Meta:
            verbose_name_plural = 'entries'
            
      def __str__(self):
            '''Entry을 나타내는 문자열 반환'''
            if len(self.text) < 50:
                  return f"{self.text}"
            else:
                  return f"{self.text[:50]}..."
      