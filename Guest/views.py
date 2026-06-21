from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Authority.models import *
from Kudumbasree.models import *
from CDS.models import *

# Create your views here.
def UserRegistration(request):
    dis=tbl_district.objects.all()
    ward=tbl_ward.objects.all()
    authoritydata=tbl_authority.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_num')
        address=request.POST.get('txt_address')
        photo=request.FILES.get('file_photo')
        password=request.POST.get('txt_pass')
        placeid=tbl_place.objects.get(id=request.POST.get('sel_place'))
        localplaceid=tbl_localplace.objects.get(id=request.POST.get('sel_localplace'))
        authoritywardid=tbl_authorityward.objects.get(id=request.POST.get('sel_ward'))
        tbl_user.objects.create(authorityward=authoritywardid,user_name=name,place=placeid,user_email=email,user_contact=contact,user_address=address,user_photo=photo,user_password=password,localplace=localplaceid)
        return render(request,'Guest/UserRegistration.html')
    else:
        return render(request,'Guest/UserRegistration.html',{'district':dis,'authoritydata':authoritydata})

def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get('did'))
    placeid=tbl_place.objects.filter(district=districtid)
    return render(request,'Guest/AjaxPlace.html',{'place':placeid})

def ajaxlocalplace(request):
    localplace=tbl_localplace.objects.filter(place=request.GET.get('pid'))
    return render(request,'Authority/AjaxLocalPlace.html',{'localplace':localplace})

def ajaxauthorityward(request):
    authorityward=tbl_authorityward.objects.filter(authority=request.GET.get('aid'))
    return render(request,'Guest/AjaxAuthorityWard.html',{'data':authorityward})

def ajaxauthority(request):
    authoritydata=tbl_authority.objects.filter(place=request.GET.get('pid'))
    return render(request,'Guest/AjaxAuthority.html',{'data':authoritydata})

def Login(request):
    if request.method=="POST":
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')
        admincount=tbl_admin.objects.filter(Admin_email=email,Admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count() 
        authoritycount=tbl_authority.objects.filter(authority_email=email,authority_password=password).count()
        kudumbasreecount=tbl_kudumbasree.objects.filter(kudumbasree_email=email,kudumbasree_password=password).count()
        cdscount=tbl_cds.objects.filter(cds_email=email,cds_password=password).count()
        adscount=tbl_ads.objects.filter(ads_email=email,ads_password=password).count()
        if admincount>0:
            admindata=tbl_admin.objects.get(Admin_email=email,Admin_password=password)
            request.session['aid']=admindata.id
            return redirect("Admin:HomePage")
        elif usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect("User:HomePage")
        elif authoritycount>0:
            authoritydata=tbl_authority.objects.get(authority_email=email,authority_password=password)
            request.session['yid']=authoritydata.id
            return redirect("Authority:HomePage")
        elif kudumbasreecount>0:
            kudumbasreedata=tbl_kudumbasree.objects.get(kudumbasree_email=email,kudumbasree_password=password)
            if kudumbasreedata.kudumbasree_status == 0:
                return render(request,'Guest/Login.html',{"msg":"Registration Verification Pending"})
            elif kudumbasreedata.kudumbasree_status == 2:
                return render(request,'Guest/Login.html',{"msg":"Registration Verification Rejected"})
            else:
                request.session['kid']=kudumbasreedata.id
                return redirect("Kudumbasree:HomePage")
        elif cdscount>0:
            cdsdata=tbl_cds.objects.get(cds_email=email,cds_password=password)
            request.session['cdsid']=cdsdata.id
            return redirect("CDS:HomePage")
        elif adscount>0:
            adsdata=tbl_ads.objects.get(ads_email=email,ads_password=password)
            request.session['adsid']=adsdata.id
            return redirect("ADS:HomePage")
        else:
            return render(request,'Guest/Login.html',{"msg":"Invalid Email or Password"})
        
    else:
        return render(request,'Guest/Login.html')

def Authority(request):
    authority=tbl_authoritytype.objects.all()
    dis=tbl_district.objects.all()
    
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_num')
        address=request.POST.get('txt_address')
        photo=request.FILES.get('file_photo')
        proof=request.FILES.get('file_proof')
        password=request.POST.get('txt_pass')
        placeid=tbl_place.objects.get(id=request.POST.get('sel_place'))
        authoritytype_id=tbl_authoritytype.objects.get(id=request.POST.get('sel_authority'))
        tbl_authority.objects.create(authority_name=name,place=placeid,authority_email=email,authority_contact=contact,authority_address=address,authority_photo=photo,authority_proof=proof,authority_password=password,authoritytype=authoritytype_id)
        return render(request,'Guest/Authority.html')
    else:
        return render(request,'Guest/Authority.html',{'district':dis,'authority':authority})

def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get('did'))
    placeid=tbl_place.objects.filter(district=districtid)
    return render(request,'Guest/AjaxPlace.html',{'place':placeid})

def index(request):
    return render(request,"Guest/Index.html")

def Kudumbasree(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')
        contact=request.POST.get('txt_num')
        localplaceid=tbl_localplace.objects.get(id=request.POST.get('sel_localplace'))
        authoritywardid=tbl_authorityward.objects.get(id=request.POST.get('sel_authward'))
        authorityid=tbl_authority.objects.get(id=request.POST.get('sel_authority'))
        authid=tbl_authority.objects.get(id=request.session['yid'])
        tbl_kudumbasree.objects.create(authorityward=authoritywardid,kudumbasree_name=name,kudumbasree_email=email,kudumbasree_password=password,kudumbasree_contact=contact,localplace=localplaceid,authority=authorityid)
    return render(request,'Guest/Kudumbasree.html',{'dis':dis})

