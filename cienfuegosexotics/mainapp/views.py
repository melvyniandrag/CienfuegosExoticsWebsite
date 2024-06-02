from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, "mainapp/index.html", context)

def peppers(request):
    context = {}
    return render(request, "mainapp/peppers.html", context)
