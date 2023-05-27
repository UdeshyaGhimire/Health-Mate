from django .urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("",views.index,name="healthapp"),
    path("about/",views.about,name="AboutUs"),
    path("consultationform/",views.consultationform,name="consultationform"),
    path("blog/",views.blog,name="blog"),
    path("ourservices/",views.ourservices,name="ourservices"),
    path("ourdoctors/",views.ourdoctors,name="ourdoctors"),
    path("base/",views.base,name="base")
]