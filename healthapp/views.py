from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'healthapp/index.html')
def about(request):
    return render(request,'healthapp/about.html')
def contactus(request):
    return HttpResponse("This is contact us")
def consultationform(request):
    return render(request, 'healthapp/consultationform.html')
