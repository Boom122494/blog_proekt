from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import CreateUserForm



def home(request):
    return render(request, 'main/index.html')



def index(request):
    return render (request, 'main/index.html')



def about(request):
    return render(request, 'main/about.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'main/register.html', context)


def LoginPage(request):
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'main/login.html', context)
