from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    category = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.title
    
