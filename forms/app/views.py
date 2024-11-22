from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

def user_def_form(req):
    if req.method == 'POST':
        form1 = User_form(req.POST)
        if form1 .is_valid():
            name = form1.cleaned_data['Name']
            age = form1.cleaned_data['age']
            email = form1.cleaned_data['email']
            data = Sample.objects.create(Name=name,Age=age,Email=email)
            data.save()
            return redirect(user_def_form)
    form=User_form()
    return render(req,'user_form.html',{'form':form})

def model_form(req):
    if req.method == 'POST':
        form1 = Model_form(req.POST)
        if form1 .is_valid():
            form1.save()
        return redirect(model_form)
    form = Model_form()
    return render(req,'model_form.html',{'form':form})