from django.db import models
# Create your models here.

class Report(models.Model):
    report_type=models.TextField()
    date = models.DateField()
    location = models.TextField()
    time=models.TimeField()
    report_title=models.TextField()
    description=models.TextField()

class Contact(models.Model):
    name=models.TextField(null=True)
    email=models.EmailField(null=True)
    phone=models.TextField(null=True)

