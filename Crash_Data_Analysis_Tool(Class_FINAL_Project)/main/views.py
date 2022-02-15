from django.shortcuts import render
from django.views import View
from django.contrib import messages
from main import models
from main import forms
import json
import sqlite3
detectorlist=[]
time=[]
conn = sqlite3.connect("trafficdata.db")
c = conn.cursor()
c.execute("select distinct DetectorID from trafficdata ")
result = c.fetchall()
for i in result:
  detectorlist.append(i[0])

c.execute("select distinct Time from trafficdata ")
result = c.fetchall()
for i in result:  
  time.append(i[0])


class Home(View):
  def get(self,request):
    return render(request, 'main/index.html',{"detector":detectorlist,"time":time})
  def post(self,request):    
    sql='select*from trafficdata where ('  
 
    DetectorID = request.POST.getlist('DetectorID')  
    FDate = request.POST['FDate']
    TDate = request.POST['TDate']
    FTime = request.POST['FTime']
    TTime = request.POST['TTime']
    print ( DetectorID)
    for j,i in enumerate(DetectorID):
      if j<len(DetectorID)-1:
        sql+='DetectorID = '+i+' or '
      else:
        sql+='DetectorID = '+i+') and '
    sql+="(Date>= '"+FDate+"' and Date<= '"+ TDate +"') and (Time<= '"+TTime+"' and Time>= '"+FTime+"')"
    sql2='select DetectorID, 100*sum(test1)/count(test1),100*sum(test2)/count(test2),100*sum(test3)/count(test3),100*sum(test4)/count(test4),100*sum(test5)/count(test5),100*sum(test6)/count(test6),100*sum(test7)/count(test7),100*sum(test8)/count(test8),100*sum(test9)/count(test9),100*sum(test10)/count(test10) from ('+sql+') foo group by DetectorID;' 
    sql3='select 1.0*sum(test1)/count(test1),1.0*sum(test2)/count(test2),1.0*sum(test3)/count(test3),1.0*sum(test4)/count(test4),1.0*sum(test5)/count(test5),1.0*sum(test6)/count(test6),1.0*sum(test7)/count(test7),1.0*sum(test8)/count(test8),1.0*sum(test9)/count(test9),1.0*sum(test10)/count(test10)from ('+sql+');'
    conn = sqlite3.connect("trafficdata.db")
    cb = conn.cursor()
    cb.execute(sql2)

    rslt = cb.fetchall()
    cb.execute(sql3)
    rslt2 = cb.fetchall()
   
  
    for i in rslt2:      
      data=list(i)
    
    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Ratio of bad data/outliers/missing values with Total Data'},
        'xAxis': {'categories': ['Test 1','Test2','Test 3','Test 4','Test 5','Test 6','Test 7','Test 8','Test 9','Test 10']},
        'series':[{'data':data,'name':'Combined by Detectors'}]
    }

    dump = json.dumps(chart)
   
    return render(request, 'main/mapresult.html',{"rslt":rslt,'chart':dump})
class Read(View):
  def get(self,request):
    return render(request, 'main/testsummary.html')
class Write(View):
  def get(self,request):
    message = list(models.Feedbacks.objects.all().values_list())
    print(message)
    return render(request, 'main/feedback.html',{'form':forms.FeedbackForm(),'msg':message})

  def post(self,request):
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for visiting')
            return render(request, 'main/feedback.html')
    else:
        form = FeedbackForm()
    return render(request, 'main/feedback.html', {'form': form})