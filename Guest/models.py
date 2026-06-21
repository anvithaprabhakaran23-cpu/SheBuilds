from django.db import models
from Admin.models import *
# from Authority.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to="Assets/File/User")
    user_password=models.CharField(max_length=30)
    user_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    localplace=models.ForeignKey(tbl_localplace,on_delete=models.CASCADE,null=True)
    authorityward=models.ForeignKey(tbl_authorityward,on_delete=models.CASCADE)
    
class tbl_kudumbasree(models.Model):
    kudumbasree_name=models.CharField(max_length=30)
    kudumbasree_email=models.CharField(max_length=30)
    kudumbasree_contact=models.CharField(max_length=30)
    kudumbasree_password=models.CharField(max_length=30)
    kudumbasree_status=models.IntegerField(default=0)
    localplace=models.ForeignKey(tbl_localplace,on_delete=models.CASCADE)
    authority=models.ForeignKey(tbl_authority,on_delete=models.CASCADE)
    authorityward=models.ForeignKey(tbl_authorityward,on_delete=models.CASCADE)