from django.shortcuts import render,redirect
from .form import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.save
        return redirect('haha')
    form = LoginForm()
    
    return render(request, 'main/login.html', {"form": form})

def haha(request):
    return render(request, 'main/haha.html')


