from django.db import models
from Admin.models import *
# Create your models here.

class tbl_cds(models.Model):
    cds_name = models.CharField(max_length=30)
    cds_email = models.CharField(max_length=30)
    cds_contact = models.CharField(max_length=30)
    cds_password = models.CharField(max_length=30)
    cds_photo = models.FileField(upload_to='Assets/CDS/')
    authorityward = models.ForeignKey(tbl_authorityward, on_delete=models.CASCADE)