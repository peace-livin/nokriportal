from django.db import models

# Create your models here.
job_titles = [
    ('engineer', 'engineer'),
    ('manager', 'manager'),
    ('admin', 'admin'),
]      

qualifications = [
    ('cse', 'cse'),
    ('btech', 'btech'),
    ('me', 'me'),   
]


class Mumbai(models.Model):
    company_name = models.CharField(max_length=100)
    job_titles = models.CharField(max_length=100, choices=job_titles)
    sal=models.IntegerField()
    qualifications = models.CharField(max_length=100, choices=qualifications)
    joining_date = models.DateField()
    location = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    
    
class Pune(models.Model):
    company_name = models.CharField(max_length=100)
    job_titles = models.CharField(max_length=100, choices=job_titles)
    sal=models.IntegerField()
    qualifications = models.CharField(max_length=100, choices=qualifications)
    joining_date = models.DateField()
    location = models.CharField(max_length=100)
    address= models.CharField(max_length=100)

class Hyderabad(models.Model):
    company_name = models.CharField(max_length=100)
    job_titles = models.CharField(max_length=100, choices=job_titles)
    sal=models.IntegerField()
    qualifications = models.CharField(max_length=100, choices=qualifications)
    joining_date = models.DateField()
    location = models.CharField(max_length=100)    
    address= models.CharField(max_length=100)
    
