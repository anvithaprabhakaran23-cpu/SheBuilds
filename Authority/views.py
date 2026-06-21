from django.shortcuts import render,redirect
from Guest.models import *
from Authority.models import*
from Kudumbasree.models import*

# Create your views here.
def HomePage(request):
    return render(request,'Authority/HomePage.html')
def MyProfile(request):
    authoritydata=tbl_authority.objects.get(id=request.session['yid'])
    return render(request,'Authority/MyProfile.html',{'authority':authoritydata})

def EditProfile(request):
    editdata=tbl_authority.objects.get(id=request.session['yid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_num')
        address=request.POST.get('txt_address')
        editdata.authority_name=name
        editdata.authority_email=email
        editdata.authority_contact=contact
        editdata.authority_address=address

        editdata.save()
        return render(request,'Authority/EditProfile.html',{'msg':'Updated'})
    else:
        return render(request,'Authority/EditProfile.html',{'editdata':editdata})

    return render(request,'Authority/EditProfile.html')

def ChangePassword(request):
    userdata=tbl_authority.objects.get(id=request.session['yid'])
    if request.method=="POST":
       password=request.POST.get('txt_oldpass')
       newpassword=request.POST.get('txt_newpass')
       retypepassword=request.POST.get('txt_pass')
       dbpass=userdata.authority_password
       if dbpass == password:
        if newpassword == retypepassword:
            userdata.authority_password = newpassword
            userdata.save()
            return render(request,'Authority/MyProfile.html',{'msg':"Updated"})
        else:
            return render(request,'Authority/ChangePassword.html',{'msg':" Password Mismatched"})

       else:
        return render(request,'Authority/ChangePassword.html',{'msg':"Enter Correct Password"})
    else:
        return render(request,'Authority/ChangePassword.html')


def ajaxplace(request):
    districtid=tbl_district.objects.get(id=request.GET.get('did'))
    placeid=tbl_place.objects.filter(district=districtid)
    return render(request,'Guest/AjaxPlace.html',{'place':placeid})

def ajaxlocalplace(request):
    localplace=tbl_localplace.objects.filter(place=request.GET.get('pid'))
    return render(request,'Authority/AjaxLocalPlace.html',{'localplace':localplace})

def MyWard(request):
    ward=tbl_ward.objects.all()
    auth=tbl_authority.objects.get(id=request.session['yid'])
    authorityward=tbl_authorityward.objects.filter(authority=auth)
    if request.method=="POST":
       wardid=tbl_ward.objects.get(id=request.POST.get('sel_ward'))
       authid=tbl_authority.objects.get(id=request.session['yid'])
       tbl_authorityward.objects.create(ward=wardid,authority=authid)
    return render(request,'Authority/MyWard.html',{'ward':ward,'authorityward':authorityward})
def  deletemyward(request,did):
        tbl_authorityward.objects.get(id=did).delete()
        return render(request,'Authority/MyWard.html',{'msg':'Deleted'})

def CDSRegistration(request):
    authority_id = request.session.get('yid')

    if not authority_id:
        return redirect('Guest:Login')

    # Get wards of this authority
    wards = tbl_authorityward.objects.filter(authority=authority_id)

    # Get CDS list for this authority (through authorityward)
    cds_list = tbl_cds.objects.filter(authorityward__authority=authority_id)

    if request.method == "POST":
        name = request.POST.get('txt_name')
        email = request.POST.get('txt_email')
        contact = request.POST.get('cds_contact')
        password = request.POST.get('txt_pass')
        photo = request.FILES.get('file_photo')
        ward_id = request.POST.get('sel_ward')

        ward = tbl_authorityward.objects.get(id=ward_id)

        tbl_cds.objects.create(
            cds_name=name,
            cds_email=email,
            cds_contact=contact,
            cds_password=password,
            cds_photo=photo,
            authorityward=ward
        )
        return redirect('Authority:CDSRegistration')

    return render(request, 'Authority/CDSRegistration.html', {
        'wards': wards,
        'cds_list': cds_list
    })

def DeleteCDS(request, id):
    tbl_cds.objects.get(id=id).delete()
    return redirect('Authority:CDSRegistration')

def Notification(request):
    authority_id = request.session.get('yid')

    authority = tbl_authority.objects.get(id=authority_id)

    notifications = tbl_notification.objects.filter(authority=authority).order_by('-id')

    if request.method == "POST":
        title = request.POST.get('txt_title')
        details = request.POST.get('txt_details')
        location = request.POST.get('txt_location')
        file = request.FILES.get('file_file')

        tbl_notification.objects.create(
            notification_title=title,
            notification_details=details,
            notification_location=location,
            notification_file=file,
            authority=authority   # ✅ only authority filled
        )

        return redirect('Authority:Notification')

    return render(request, 'Authority/Notification.html', {
        'notifications': notifications
    })


def DeleteNotification(request, id):
    tbl_notification.objects.get(id=id).delete()
    return redirect('Authority:Notification')

def CompleteNotification(request, id):
    notification = tbl_notification.objects.get(id=id)
    notification.notification_status = 1   # ✅ Completed / Active
    notification.save()
    return redirect('Authority:Notification')

def logout(request):
    del request.session['yid']
    return redirect("Guest:Login")