from django.db import models
# Create your models here.

class Report(models.Model):
    report_type=models.TextField()
    date = models.DateField()
    location = models.TextField()
    time=models.TimeField()
    report_title=models.TextField()
    description=models.TextField()

