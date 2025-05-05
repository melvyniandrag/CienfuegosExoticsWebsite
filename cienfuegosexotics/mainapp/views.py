from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, "mainapp/index.html", context)
    
def about(request):
    context = {}
    return render(request, "mainapp/aboutus.html", context)

def tomatoes(request):
    context = {}
    return render(request, "mainapp/tomatoes.html", context)

def mantises(request):
    context = {}
    return render(request, "mainapp/mantises.html", context)

def peppers(request):
    context = {}
    return render(request, "mainapp/peppers.html", context)

def contact(request):
    context = {}
    return render(request, "mainapp/contact.html", context)

def learning(request):
    context = {}
    return render(request, "mainapp/learning.html", context)
