from django.shortcuts import render
from django.views import View
from main import models
from main import forms

# Create your views here.
# as migration is not working properly, i could not change the variable name

class Home(View):
  
  def get(self,request):
    std = list(models.Student.objects.all().values_list())
    quizes=list(models.Quizes.objects.all().values_list())    
    return render(request, 'main/index.html',{"row":std,"col":quizes})
  def post(self,request):
    quizes=list(models.Quizes.objects.all().values_list()) 
    std = list(models.Student.objects.all().values_list())
    out = request.POST.dict()
    
    print (out)
    return render(request, 'main/index.html',{"row":std,"col":quizes,"out":out})

class Person(View):
  def get(self,request):
    people = list(models.Quizes.objects.all().values_list())
    return render(request, 'main/person.html', {"form":forms.QuizForm(),"people":people})
  def post(self,request):
    form = forms.QuizForm(request.POST)
    if form.is_valid(): 
      form.save()      
      form = forms.QuizForm()
    quizes=list(models.Quizes.objects.all().values_list()) 
    people = list(models.Student.objects.all().values_list())
    return render(request, 'main/index.html',{"row":people,"col":quizes,})

class friend(View):
  def get(self,request):
    friends = list(models.Student.objects.all().values_list())
    return render(request, 'main/student.html',{"friends":friends,"form":forms.StudentForm()})
  def post(self,request):
    form = forms.StudentForm(request.POST)
    if form.is_valid():
      form.save()
      form = forms.StudentForm()    
    quizes=list(models.Quizes.objects.all().values_list()) 
    people = list(models.Student.objects.all().values_list())
    return render(request, 'main/index.html',{"row":people,"col":quizes})