from django.shortcuts import render
from django.views import View
things = []

# Create your views here.
class Home(View):
  def get(self,request):
    return render(request, 'main/index.html')
  def post(self,request):
    date = request.POST["date"]
    time = request.POST["time"] 
    location = request.POST["location"]    
    things.append((str(date),str(time),location))
    message=str(things) 
    return render(request, 'main/result.html',{"message":message,"myList":things})

