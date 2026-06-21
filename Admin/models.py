from django.db import models
# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_admin(models.Model):
    Admin_name=models.CharField(max_length=30)
    Admin_email=models.CharField(max_length=30)
    Admin_password=models.CharField(max_length=30)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_localplace(models.Model):
    localplace_name=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_ward(models.Model):
    ward_number=models.CharField(max_length=30)
    
class tbl_authoritytype(models.Model):
    authoritytype_name=models.CharField(max_length=30)

class tbl_authority(models.Model):
    authority_name=models.CharField(max_length=30)
    authority_email=models.CharField(max_length=30)
    authority_contact=models.CharField(max_length=30)
    authority_address=models.CharField(max_length=30)
    authority_photo=models.FileField(upload_to="Assets/File/User")
    authority_proof=models.FileField(upload_to="Assets/File/User")
    authority_password=models.CharField(max_length=30)
    authority_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    authoritytype=models.ForeignKey(tbl_authoritytype,on_delete=models.CASCADE)

class tbl_authorityward(models.Model):
    ward=models.ForeignKey(tbl_ward,on_delete=models.CASCADE) 
    authority=models.ForeignKey(tbl_authority,on_delete=models.CASCADE)
