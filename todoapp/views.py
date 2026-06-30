from django.shortcuts import render,redirect
from .models import todo
# Create your views here.
def home(request):
    todos=todo.objects.all()
    return render(request,'index.html',{'todos':todos})

def add_task(request):
    if request.method=='POST':
        a=request.POST.get('taskname')
        b=request.POST.get('date')
        todo.objects.create(taskname=a,date=b)
        return redirect('home')
    return render(request,'add_task.html')

def delete_task(request,id):
    a=todo.objects.filter(id=id)
    a.delete()
    return redirect('home')

def update_task(request,id):
    a=todo.objects.get(id=id)
    if request.method=='POST':
        a.taskname=request.POST.get('update-name')
        a.date=request.POST.get('update-date')
        a.save()
        return redirect('home')
    return render(request,'update.html',{'a':a})