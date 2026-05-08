from django.http import HttpResponse
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

def robots_txt(request):
    content = """
                User-agent: *
                Allow: /
                Sitemap: https://pardymobilemechanics.co.za/sitemap.xml
            """
    return HttpResponse(content, content_type="text/plain")