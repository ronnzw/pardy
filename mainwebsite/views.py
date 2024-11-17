from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request,'home.html', context=context)

def services(request):
    context = {}
    return render(request,'services.html', context=context)

def contacts(request):
    context = {}
    return render(request,'contact.html', context=context)

def about(request):
    context = {}
    return render(request,'about.html', context=context)