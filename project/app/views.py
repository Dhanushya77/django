from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
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
def fun8(req):
    a="python"
    b=['orange','apple','banana']
    c=('green','yellow','red')
    d=777
    e={'fruit':'apple','color':'red'}
    l=[1,2,3,4,5,6,7,8]
    
    
    user={'name':'anu','age':22},{'name':'geethu','age':24},{'name':'anju','age':32},{'name':'akhil','age':42},{'name':'bodhi','age':20},{'name':'joel','age':50},
    l1=[]
    l2=[]
    for i in user:
        if i['age']<30:
            l1.append(i)
        else:
            l2.append(i)
    return render(req,'demo.html',{'a':a,'b':b,"c":c,"d":d,"e":e,"l":l,"user":user,"l1":l1,"l2":l2})

std=[{'roll_no': '1', 'name': 'dhanushya', 'age': '22'}, {'roll_no': '2', 'name': 'anu', 'age': '24'}, {'roll_no': '3', 'name': 'adhi', 'age': '23'}]
def add_std(req):
    if req.method == 'POST':
        roll = req.POST['roll_no']
        name = req.POST['name']
        age = req.POST['age']
        # std.append({'roll_no':roll,'name':name,"age":age})
        # print(std)
        data = Student.objects.create(roll_no=roll,name=name,age=age)
        data.save()
        return redirect(add_std)
    else:
        data = Student.objects.all()
        return render(req,'add_std.html',{"std":data})
def edit_std(req,id):
    # print(id)
    # for i in std:
    #     if i['roll_no'] == id:
    #         student=i
    #         print(student)
    data = Student.objects.get(pk=id)
            
    if req.method == 'POST':
        roll = req.POST['roll_no']
        name = req.POST['name']
        age = req.POST['age']
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age)
        # student['roll_no'] = roll
        # student['name'] = name
        # student['age'] = age
        return redirect(add_std)
    else:
        return render(req,'edit.html',{'data':data})
        
def delete_std(req,id):
    data = Student.objects.get(pk=id)
    data.delete()
    # for i in std:
    #     if i['roll_no'] == id:
    #         std.remove(i)
    return redirect(add_std)
            