from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(req):
    return HttpResponse("welcome all")
def fun2(req,salary,year):
    if year>5:
        salary='bonus is ',0.05*salary
    else:
        salary='no bonus'
    return HttpResponse(salary,year)
def fun3(req,digit):
    digit=digit%10
    if digit%3 == 0:
        digit='divisible by 3'
    else:
        digit='not divisible by 3'
    return HttpResponse(digit)
def fun4(req,unit):
    if unit<=100:
        unit='no charge'
    elif 100<unit<=200:
        unit='charge is ',(unit-100)*5 
    else:
        unit='charge is ',500+(unit-200)*10
    return HttpResponse(unit)
def fun5(req,city):
    if city=='delhi':
        city='Red Fort'
    elif city=='agra':
        city='Taj Mahal'
    elif city=='jaipur':
        city='Jal Mahal'
    else:
        city='invalid'
    return HttpResponse(city)
def fun6(req,no):
    if no==1:
        no='SUNDAY'
    elif no==2:
        no='MONDAY'
    elif no==3:
        no='TUESDAY'
    elif no==4:
        no='WEDNESDAY'
    elif no==5:
        no='THURSDAY'
    elif no==6:
        no='FRIDAY'
    elif no==7:
        no='SATURDAY'
    else:
        no='invalid'
    return HttpResponse(no)
def fun7(req,cp):
    if cp<=50000:
        cp='Tax is ',0.05*cp
    elif 50000<cp<=100000:
        cp='Tax is ',0.1*cp
    else:
        cp='Tax is ',0.15*cp
    return HttpResponse(cp)