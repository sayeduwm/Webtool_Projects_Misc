from django.db import models
from django.core.validators import MinValueValidator



# .......As migration is not working.I could not rename teh class name and filed.........
# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length=20, primary_key=True)
  age = models.IntegerField(validators=[MinValueValidator(1,"Age must be postive")])
  
  time = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
  first = models.ForeignKey(Person, related_name="firstPerson", on_delete=models.CASCADE)
  second = models.ForeignKey(Person, related_name="secondPerson",on_delete=models.CASCADE)
  time = models.DateTimeField(auto_now=True)

class Student(models.Model):
  FirstName = models.CharField(max_length=20)
  LastName = models.CharField(max_length=20)
  ID = models.IntegerField(validators=[MinValueValidator(1,"Age must be postive")],primary_key=True)
 

class Quizes(models.Model):
  QuizName = models.CharField(max_length=20,primary_key=True)
  MaxPoint = models.IntegerField(default=0)
