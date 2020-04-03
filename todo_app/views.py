from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Todo
from django.urls import reverse
from .models import Todo
from django.utils import timezone
from django.shortcuts import redirect
from .forms import SearchForm

# Create your views here.
def index(request):
    form=SearchForm(request.POST or None)
    if form.is_valid():
        form.save()

    ls=request.POST.get("todo")
    # todolist=Todo.objects.create(text=ls)
    # print(Todo.objects.all().count())
    # context={'form':form}
    todo_items=Todo.objects.all().order_by('-added_date')
    context={'todo_items':todo_items,'form':form}
    return render(request,'todo_app/todolist.html',context)


def todolist(request):
    form=SearchForm(request.POST or None)
    if form.is_valid():
        form.save()

    ls=request.POST.get("todo")
    # todolist=Todo.objects.create(text=ls)
    # print(Todo.objects.all().count())
    context={'form':form}
    # context={'ls':ls,
    #          'todolist':todolist,}
    render(request,'todo_app/todolist.html',context)
    # return HttpResponseRedirect("/")
    # render(request,'todo_app/todolist.html',context)


def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect("/")
