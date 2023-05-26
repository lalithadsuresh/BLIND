from django.shortcuts import render

def index(request):
    return render(request, 'myproject/myapp/templates/index.html')

def signup(request):
    return render(request, 'myproject/myapp/templates/signup.html')

    