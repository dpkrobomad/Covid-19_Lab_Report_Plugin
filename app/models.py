from django.db import models
from LabReport.settings import BASE_DIR


# Create your models here.

class Labreport (models.Model):
    Name = models.CharField(max_length=40)
    Phone = models.IntegerField()
    Lab_Number = models.IntegerField()
    report = models.FileField(upload_to='LabReport/media/')
