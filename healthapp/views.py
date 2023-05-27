from django.shortcuts import render
from django.http import HttpResponse
from .models import doctor
from math import ceil

# Create your views here.


def index(request):
    return render(request, 'healthapp/index.html')


def about(request):
    return render(request, 'healthapp/about.html')


def ourdoctors(request):
    allDocs = []
    departdocs = doctor.objects.values('department', 'id')
    cats = {item['department'] for item in departdocs}
    for cat in cats:
        doc = doctor.objects.filter(department=cat)
        n = len(doc)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allDocs.append([doc, range(1, nSlides), nSlides])
    params = {'allDocs': allDocs}
    return render(request, 'healthapp/ourdoctors.html', params)
    # doctors = doctor.objects.all()
    # n = len(doctors)
    # nSlides = n//4 + ceil((n/4) + (n//4))
    # #   params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'doctor': doctors}
    # allDocs = [[doctors, range(1, nSlides), nSlides], [
    #     doctors, range(1, nSlides), nSlides]]
    # params = {'allDocs': allDocs}


def consultationform(request):
    return render(request, 'healthapp/consultationform.html')


def blog(request):
    return render(request, 'healthapp/blog.html')
