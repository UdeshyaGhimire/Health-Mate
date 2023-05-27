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
def blog(request):
    return render(request, 'healthapp/blog.html')
def ourservices(request):
    return render(request, 'healthapp/ourservices.html')
def ourdoctors(request):
    return render(request, 'healthapp/ourdoctors.html')
def base(request):
    return render(request, 'healthapp/base.html')

