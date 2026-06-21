from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import*
from User.models import*
# Create your views here.
def District(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        tbl_district.objects.create(district_name=name)
        return render(request,'Admin/District.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/District.html',{"district":dis})

def  deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':'Deleted'})
def  editdistrict(request,eid):
    edit=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get('txt_name')
        edit.district_name=name
        edit.save()
        return render(request,'Admin/District.html',{'msg':'Updated'})
    else:
        return render(request,'Admin/District.html',{'editdata':edit})

def Category(request):
    cat=tbl_category.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        tbl_category.objects.create(category_name=name)
        return render(request,'Admin/Category.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/Category.html',{"category":cat})

def  delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return render(request,'Admin/Category.html',{'msg':'Deleted'})
def  editcategory(request,mid):
    edit=tbl_category.objects.get(id=mid)
    if request.method=="POST":
        name=request.POST.get('txt_name')
        edit.category_name=name
        edit.save()
        return render(request,'Admin/Category.html',{'msg':'Updated'})
    else:
        return render(request,'Admin/Category.html',{'editdata':edit})

def AdminRegistration(request):
    reg=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        tbl_admin.objects.create(Admin_name=name,Admin_email=email,Admin_password=password)
        return render(request,'Admin/AdminRegistration.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/AdminRegistration.html',{"admin":reg})
        
def  deladmin(request,aid):
    tbl_admin.objects.get(id=aid)
    return render(request,'Admin/AdminRegistration.html',{'msg':'Deleted'})
def  editadmin(request,kid):
    edit=tbl_admin.objects.get(id=kid)
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        edit.Admin_name=name
        edit.Admin_email=email
        edit.Admin_password=password
        edit.save()
        return render(request,'Admin/AdminRegistration.html',{'msg':'Updated'})
    else:
        return render(request,'Admin/AdminRegistration.html',{'editdata':edit})

def Place(request):
    dis=tbl_district.objects.all()
    plc=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        districtid=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=name,district=districtid)
        return render(request,'Admin/Place.html')
    else:
        return render(request,'Admin/Place.html',{'district':dis,'place':plc})

def  delplace(request,did):
        tbl_place.objects.get(id=did).delete()
        return render(request,'Admin/Place.html',{'msg':'Deleted'})
def  editplace(request,eid):
    dis=tbl_district.objects.all()
    edit=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get('txt_name')
        edit.place_name=name
        edit.save()
        return render(request,'Admin/Place.html',{'msg':'Updated'})
    else:
        return render(request,'Admin/Place.html',{'editdata':edit,'district':dis})

def Subcategory(request):
    dis=tbl_category.objects.all()
    sub=tbl_subcategory.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        categoryid=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=name,category=categoryid)
        return render(request,'Admin/Subcategory.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/Subcategory.html',{'category':dis,'subcategory':sub})
    
def  delsubcategory(request,did):
        tbl_subcategory.objects.get(id=did).delete()
        return render(request,'Admin/Subcategory.html',{'msg':'Deleted'})
def  editsubcategory(request,eid):
    cat=tbl_category.objects.all()
    edit=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get('txt_name')
        edit.subcategory_name=name
        edit.save()
        return render(request,'Admin/Subcategory.html',{'msg':'Updated'})
    else:
        return render(request,'Admin/Subcategory.html',{'editdata':edit,'category':cat})

def HomePage(request):
    usercount = tbl_user.objects.count()
    kudumbasreecount = tbl_kudumbasree.objects.count()
    cdscount = tbl_cds.objects.count()
    adscount = tbl_ads.objects.count()
    context = {
        "usercount":usercount,
        "kudumbasreecount":kudumbasreecount,
        "cdscount":cdscount,
        "adscount":adscount
    }
    return render(request,'Admin/HomePage.html',context)
def UserList(request):
    userdata=tbl_user.objects.filter(user_status=0)
    accept=tbl_user.objects.filter(user_status=1)
    reject=tbl_user.objects.filter(user_status=2)
    return render(request,'Admin/UserList.html',{'userdata':userdata,'accept':accept,'reject':reject})
def Acceptuserlist(request,aid):
    accept=tbl_user.objects.get(id=aid)
    accept.user_status=1
    accept.save()
    return render(request,'Admin/UserList.html',{'msg':'Accepted'})
def rejectuserlist(request,rid):
    reject=tbl_user.objects.get(id=rid)
    reject.user_status=2
    reject.save()
    return render(request,'Admin/UserList.html',{'msg':'Rejected'})

def Reply(request,id):
    rpl=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        reply=request.POST.get('txt_reply')
        rpl.complaint_reply=reply
        rpl.complaint_status=1
        rpl.save()
        return render(request,'Admin/Reply.html',{"msg":"replied"})
    else:
        return render(request,'Admin/Reply.html')


def ViewComplaint(request):
    complaint=tbl_complaint.objects.all()
    return render(request,'Admin/ViewComplaint.html',{"complaint":complaint})

def ViewFeedback(request):
    feedback=tbl_feedback.objects.all()
    return render(request,'Admin/ViewFeedback.html',{"feedback":feedback})

def LocalPlace(request):
    dis=tbl_district.objects.all()
    local=tbl_localplace.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_localplace')
        placeid=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_localplace.objects.create(localplace_name=name,place=placeid)
        return render(request,'Admin/LocalPlace.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/LocalPlace.html',{"district":dis,"localplace":local})
def  dellocalplace(request,did):
    tbl_localplace.objects.get(id=did).delete()
    return render(request,'Admin/LocalPlace.html',{'msg':'Deleted'})

def Ward(request):
    ward=tbl_ward.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_ward')
        tbl_ward.objects.create(ward_number=name)
        return render(request,'Admin/Ward.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/Ward.html',{"ward":ward})
def  delward(request,did):
    tbl_ward.objects.get(id=did).delete()
    return render(request,'Admin/Ward.html',{'msg':'Deleted'})

def AuthorityType(request):
    Authoritytype=tbl_authoritytype.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_authority')
        tbl_authoritytype.objects.create(authoritytype_name=name)
        return render(request,'Admin/AuthorityType.html',{'msg':'Inserted'})
    else:
        return render(request,'Admin/AuthorityType.html',{"Authoritytype":Authoritytype})

def  delauthority(request,did):
    tbl_authoritytype.objects.get(id=did).delete()
    return render(request,'Admin/AuthorityType.html',{'msg':'Deleted'})

def  editauthority(request,eid):
    edit=tbl_authoritytype.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get('txt_authority')
        edit.authoritytype_name=name
        edit.save()
        return render(request,'Admin/AuthorityType.html',{'msg':'Updated'})
    else:
        return render(request,'Admin/AuthorityType.html',{'editdata':edit})

def logout(request):
    del request.session['aid']
    return redirect("Guest:Login")