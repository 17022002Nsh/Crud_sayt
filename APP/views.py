from django.shortcuts import render, redirect
from .models import Talim

def home(request):
    tasks=Talim.objects.all()
    context={
        'tasks':tasks
    }
    return  render(request , 'index.html', context)

def yaratish(request):
    if request.method=="POST":
        title=request.POST.get("title")
        soni=Talim(
            Ism_Familiya=title
        )
        soni.save() 
        return redirect("home")
    return render(request , 'knop.html')

def uzgartirish(request, pk):
    todo=Talim.objects.get(id=pk)
    context={
        'todo':todo
    }
    if request.method =="POST" :
        text=request.POST.get("title")
        is_done=request.POST.get("is_done")
        print(is_done)
        todo.Ism_Familiya=text
        todo.is_done=bool(is_done)
        todo.save()
        return redirect ("home")
        
    return render(request, 'edit.html' ,context)


def delete_todo(request, pk):
    if not request.user.is_authenticated:
        return redirect("login")
    todo = Talim.objects.get(id=pk)
    todo.delete()
    return redirect("home")


