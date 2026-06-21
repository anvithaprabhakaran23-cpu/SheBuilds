from django.db import models
from Guest.models import*
from Kudumbasree.models import*
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=30,null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)  

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=30)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)   

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.IntegerField(default=0)
    booking_amount=models.CharField(max_length=30)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    
class tbl_cart(models.Model):
    cart_quantity=models.IntegerField(default=1)
    cart_status=models.IntegerField(default=0)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)