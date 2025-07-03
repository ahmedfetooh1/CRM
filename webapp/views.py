from django.shortcuts import render ,redirect
from .forms import CreateUserForm , LoginForm ,CreateRecordForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import Record
# Create your views here.
def index(request):
    return render(request , 'web/index.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {
        'form':form
    }

    return render(request,'web/register.html',context)


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user is not None :
            login(request,user)
            return redirect('dashboard')
    else:
        form = LoginForm()

    context = {
        'form':form
    }

    return render(request,'web/login.html',context)



@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request,'web/dashboard.html',context={'record':records})



def my_logout(request):
    logout(request)
    return redirect('login')


def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else :
        form = CreateRecordForm()
    
    context = {
        'form':form
    }
    return render(request,'web/create-record.html',context)