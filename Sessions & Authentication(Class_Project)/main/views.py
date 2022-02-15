from django.shortcuts import render, redirect
from django.contrib import messages,auth
from .forms import CustomUserCreationForm
from django.views import View
from main import models
from django.contrib.auth.decorators import login_required

# Create your views here.

username="anony"
def home(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':        
        f =  CustomUserCreationForm(request.POST)       
        if f.is_valid():
            f.save()
            print (f)
            messages.success(request, 'Account created successfully')
           # return redirect('login') 
    else:
        f = CustomUserCreationForm() 
    return render(request, 'register.html', {'form': f})

def login(request):
    #if request.user.is_authenticated():
       # return redirect('admin_page') 
    if request.method == 'POST':
        
        username1 = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username1, password=password)
 
        if user is not None:
            # correct username and password login the user
            
            global username 
            username=username1 
            request.session['username'] = username 
            auth.login(request, user)           
            print (user)
            request.session.set_expiry(3)          
            return redirect('logout') 
        else:
            messages.error(request, 'Error wrong username/password') 
    return render(request, 'login.html')
 


def admin_page(request):
    #if not request.user.is_authenticated():
       # return redirect('login')
    return render(request, 'admin_page.html')


class Home(View):
  def get(self, request):
    if username!='@#$':
      print(username)
      #n = request.session.get(username,"")
      #print(n)
      u = models.User.objects.get(name=username)
  
      #c = 0
    
      data=models.User.objects.all()
      print (data)
      #request.session["name"]=u.name
      #request.session.set_expiry(5)
      return render(request, 'index.html',{"count":u.count,"name":u.name,"m":data})
    else:
      data=models.User.objects.all()
      for i in data:
        print (i.name)
      return render(request, 'index.html',{"m":data})
  
  def post(self, request):
    
    n = request.POST.get("name","")
    if models.User.objects.filter(name=username).exists():
      u = models.User.objects.get(name=username)
      u.count = u.count +1
    else:
      u = models.User(name=username,count=1)
    u.save()
    
    data=models.User.objects.all()
    request.session["name"]=u.name
    request.session.set_expiry(5)
    return render(request, 'index.html',{"count":u.count,"name":u.name,"m":data})
 
def logout(request):    
    auth.logout(request)
        
    return render(request,'logout.html')