from django.forms import ModelForm
from main import models
 
class FriendForm(ModelForm):
  class Meta:
    model = models.Friendship
    fields = "__all__"
    
class PersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = ['name', 'age']
class StudentForm(ModelForm):
    class Meta:
        model = models.Student
        fields = ['FirstName', 'LastName','ID']

class QuizForm(ModelForm):
    class Meta:
        model = models.Quizes
        fields = ['QuizName','MaxPoint']