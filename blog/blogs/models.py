from django.db import models
from authors.models import Author



class Blog(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
  return self.title 


