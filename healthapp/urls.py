from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="healthapp"),
    path("about/", views.about, name="AboutUs"),
    path("ourdoctors/", views.ourdoctors, name="ourdoctors"),
    path("consultationform/", views.consultationform, name="consultation"),
    path("blog/", views.blog, name="blog")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
