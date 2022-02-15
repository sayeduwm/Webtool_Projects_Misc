from django.db import models
class Feedbacks(models.Model):
  Name = models.CharField(max_length=120)
  email = models.EmailField()
  Response = models.TextField()
  Happy = models.BooleanField()
  
  date = models.DateField(auto_now_add=True)

 

# Create your models here.