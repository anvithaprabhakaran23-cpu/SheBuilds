from django.db import models
from Admin.models import*
from Guest.models import*
from Authority.models import*
from CDS.models import*
# Create your models here.
class tbl_meeting(models.Model):
   meeting_details=models.CharField(max_length=30)
   meeting_date=models.DateField(auto_now_add=True)
   meeting_time=models.TimeField()
   meeting_todate=models.DateField()
   meeting_location=models.CharField(max_length=30)
   meeting_status=models.IntegerField(default=0)
   kudumbasree=models.ForeignKey(tbl_kudumbasree,on_delete=models.CASCADE) 
   meeting_url=models.CharField(max_length=1000, null=True)

class tbl_members(models.Model):
   members_status=models.IntegerField(default=0)
   user=models.ForeignKey(tbl_user,on_delete=models.CASCADE) 
   kudumbasree=models.ForeignKey(tbl_kudumbasree,on_delete=models.CASCADE) 

class tbl_notification(models.Model):
   notification_title=models.CharField(max_length=30)
   notification_details=models.CharField(max_length=30)
   notification_location=models.CharField(max_length=30)
   notification_file=models.FileField(upload_to="Assets/File/Notification/")
   notification_status=models.IntegerField(default=0)
   kudumbasree=models.ForeignKey(tbl_kudumbasree,on_delete=models.CASCADE,null=True)
   authority=models.ForeignKey(tbl_authority,on_delete=models.CASCADE,null=True)
   cds=models.ForeignKey(tbl_cds,on_delete=models.CASCADE,null=True)
   ads=models.ForeignKey(tbl_ads,on_delete=models.CASCADE,null=True)

class tbl_product(models.Model):
   product_name=models.CharField(max_length=30)
   product_details=models.CharField(max_length=30)
   product_price=models.CharField(max_length=30)
   product_file=models.FileField(upload_to="Assets/File/User")
   category=models.ForeignKey(tbl_category,on_delete=models.CASCADE) 
   kudumbasree=models.ForeignKey(tbl_kudumbasree,on_delete=models.CASCADE)

class tbl_stock(models.Model):
   stock_count=models.CharField(max_length=30)
   stock_status=models.IntegerField(default=0)
   product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
   gallery_photo=models.FileField(upload_to="Assets/File/User")
   product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_attendance(models.Model):
   attendance_date=models.DateField(auto_now_add=True)
   attendance_status=models.IntegerField(default=0)
   meeting=models.ForeignKey(tbl_meeting,on_delete=models.CASCADE)
   member=models.ForeignKey(tbl_members,on_delete=models.CASCADE)

class tbl_fine(models.Model):
   fine_amount=models.IntegerField(default=0)
   fine_date=models.DateField(auto_now_add=True)
   fine_status=models.IntegerField(default=0)
   member=models.ForeignKey(tbl_members,on_delete=models.CASCADE)

class tbl_saving(models.Model):
   saving_date=models.DateField(auto_now_add=True)
   saving_status=models.IntegerField(default=0)
   saving_amount=models.IntegerField(default=0)
   member=models.ForeignKey(tbl_members,on_delete=models.CASCADE)
   
class tbl_chit(models.Model):
   chit_date=models.DateField(auto_now_add=True)
   chit_status=models.IntegerField(default=0)
   chit_amount=models.IntegerField(default=0)
   chit_totalamount=models.IntegerField(default=0)
   kudumbasree=models.ForeignKey(tbl_kudumbasree,on_delete=models.CASCADE)

class tbl_chitmembers(models.Model):
   chitmembers_status = models.IntegerField(default=0)
   member = models.ForeignKey(tbl_members, on_delete=models.CASCADE)
   chit = models.ForeignKey(tbl_chit, on_delete=models.CASCADE)
   chitmembers_date = models.DateField(null=True)