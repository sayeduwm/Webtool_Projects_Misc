from django.shortcuts import render
from django.views import View
#from django import forms

# Create your views here.
class Home(View):
  def get(self, request):
      
      return render(request, 'main/index.html')


  def post(self, request):
      listValues={
          "heightFtError1":"",
          "heightFtError2":"",
          "heightInError1":"",
          "heightInError2":"",
          "weightError1":"",
          "weightError2":""}
      countErrorNumber=0


      name=str(request.POST["name"])
      heightFeet = request.POST["heightFeet"]
      heightInches = request.POST["heightInches"]
      weightLb = request.POST["weight"]
      
      try:
        heightFt=int(heightFeet)
        if  heightFt>=0:
           heightFt=heightFt 
        else:
           listValues["heightFtError1"]=" Error: Negative Height not allowed"
           countErrorNumber+=1

      except:
         listValues["heightFtError2"]="Error:Input Height(Feet) is not integer e.g: 5"
         countErrorNumber+=1
         
        

      
      try:
        heightIn=int(heightInches)
        if  heightIn>=0:
           heightIn=heightIn
        else:
            listValues["heightInError1"]=" Error:Negative Height not allowed"
            countErrorNumber+=1
      except:
         listValues["heightInError2"]=("Error:Input Height(inches) is not integer e.g: 3")
         countErrorNumber+=1

      
      try:
        weight=int(weightLb)
        if  weight>=0:
          weight=weight
           
        else:
            listValues["weightError1"] =" Error: Negative Weight not allowed"
            countErrorNumber+=1
      except:
        listValues["weightError2"] ="Error: Input Weight(lb) is not integer e.g: 110"
        countErrorNumber+=1

      if countErrorNumber==0:
        if heightFt>0 or heightIn>0:
          BMI = 703*weight/ (heightFt*12+heightIn)**2
          return render(request, 'main/response.html',{"name":name,"info":"'s BMI  is ","BMI":str(BMI)})
        else:
          return render(request, 'main/response.html',
          {
          "heightFtError":" Error: Height value should be greater than 0",
          })
      else:
        return render(request, 'main/response.html',
        {
          
          "heightFtError1":listValues["heightFtError1"],
          "heightFtError2":listValues["heightFtError2"],
          "heightInError1":listValues["heightInError1"],
          "heightInError2":listValues["heightInError2"],
          "weightError1":listValues["weightError1"],
          "weightError2":listValues["weightError2"]
        })
def bmi(request):
      
      return render(request, 'main/index.html')


