from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import Taskform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'showtask'

class Taskdetailsview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your views here.
def add(request):
    showtask = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'showtask':showtask})
# def detail(request):
#     task = Task.objects.all()
#     return render(request,'details.html',{'task':task})
def delete(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task = Task.objects.get(id=id)
    f = Taskform(request.POST or None , instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':f})