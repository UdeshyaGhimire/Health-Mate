from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
department = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Astrology', 'Astrology'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
)


class doctor(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to='healthApp/images')
    location = models.CharField(max_length=100)
    shift_start_time = models.CharField(max_length=10)
    shift_end_time = models.CharField(max_length=10)
    qualification_name = models.CharField(max_length=100)
    nmc_number = models.CharField(max_length=10, default="")
    institute_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(choices=department, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name
