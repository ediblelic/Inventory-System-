from distutils.log import error
from email import message
from multiprocessing import context
from pydoc import pager
from pyexpat.errors import messages
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.template import TemplateDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {
        'total_products':0,
        'listaprodukata': ['dsadsad','dsadsad','dsada']
    }
    return render(request,"main/home.html",context)
@login_required(login_url='login')
def brands(request):
    return render(request,'main/index_brands.html',{})
@login_required(login_url='login')
def attributes(request):
    return render(request,'main/index_attributes.html',{})
@login_required(login_url='login')
def category(request):
    return render(request,'main/index_category.html',{})
@login_required(login_url='login')
def reports(request):
    return render(request,'main/index_reports.html',{})
@login_required(login_url='login')
def stores(request):
    return render(request,'main/index_stores.html',{})
@login_required(login_url='login')
def groups(request):
    return render(request,'main/index_groups.html',{})

def reg(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            form.save()
            return redirect('../login')
    try:
        return render(request,'main/index_register.html',{'form':form})
    except ValueError:
        HttpResponse(request,'ERROR 500')
def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        else:
            messages.info(request,'Username OR password incorrect!')
            return render(request,'main/index_login.html',{})
        try:
            return redirect('index')
        except AttributeError:
            pass
    return render(request,'main/index_login.html',{})
def logoutPage(request):
    logout(request)
    try:
        return redirect('login')
    except ValueError:
        pass




    