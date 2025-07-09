from django.shortcuts import render ,redirect , get_object_or_404
from .forms import CreateUserForm , LoginForm ,CreateRecordForm ,UpdateRecordForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request , 'web/index.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registeration is successfully.")
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
            messages.success(request, "Login is successfully.")
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






def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record is created.")
            return redirect('dashboard')
    else :
        form = CreateRecordForm()
    
    context = {
        'form':form
    }
    return render(request,'web/create-record.html',context)

@login_required(login_url='login')
def view_record(request,id):
    all_records = get_object_or_404(Record ,id=id)

    context = {
        'record':all_records ,
    }

    return render(request,'web/view_record.html',context)



@login_required(login_url='login')
def update_record(request,record_id):
    record = get_object_or_404(Record,id=record_id)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record is updated.")
            return redirect('dashboard')
        
    context ={
        'form':form
    }
    return render(request,'web/update-record.html',context)


@login_required(login_url='login')
def delete_record(request , record_id):
    record = get_object_or_404(Record,id = record_id)
    record.delete()
    messages.success(request, "Record is deleted.")
    return redirect('dashboard')


logger = logging.Logger(__name__)
@login_required(login_url='login')
def search(request):
    qeury = request.GET.get('qeury')
    results = []
    try :
        if qeury :
            results = Record.objects.filter(Q(first_name__icontains = qeury)|Q(id__icontains=qeury))
    except Exception as e :
        logger.error('Error during search %s', e) 
    return render(request , 'web/search.html',context={
        'results':results ,
        'qeury':qeury,
    })

def my_logout(request):
    logout(request)
    messages.success(request, "Logout is successfully.")
    return redirect('login')

def custom_page_not_found(request,exception):
    return render(request,'web/404.html',status=404)