from django.shortcuts import render

def home(request):
    return render(request, 'django/home.html')