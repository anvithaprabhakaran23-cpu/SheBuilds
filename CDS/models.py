from django.db import models
from Admin.models import *
# Create your models here.

class tbl_ads(models.Model):
    ads_name = models.CharField(max_length=30)
    ads_email = models.CharField(max_length=30)
    ads_contact = models.CharField(max_length=30)
    ads_password = models.CharField(max_length=30)
    ads_photo = models.FileField(upload_to='Assets/ADS/')
    authorityward = models.ForeignKey(tbl_authorityward, on_delete=models.CASCADE)
    localplace =  models.ForeignKey(tbl_localplace, on_delete=models.CASCADE)