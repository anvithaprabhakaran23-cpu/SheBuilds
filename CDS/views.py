from django.shortcuts import render,redirect
from Authority.models import *
from CDS.models import *
from Guest.models import *
from Kudumbasree.models import *
# Create your views here.

def HomePage(request):
    return render(request,'CDS/HomePage.html')

def MyProfile(request):
    cdsdata=tbl_cds.objects.get(id=request.session['cdsid'])
    if request.method=="POST":
        cdsdata.cds_name=request.POST.get('txt_name')
        cdsdata.cds_email=request.POST.get('txt_email')
        cdsdata.cds_contact=request.POST.get('txt_num')
        cdsdata.save()
        return render(request,'CDS/MyProfile.html',{'msg':'Updated'})
    return render(request,'CDS/MyProfile.html',{'cds':cdsdata})

def ChangePassword(request):
    cdsdata=tbl_cds.objects.get(id=request.session['cdsid'])
    if request.method=="POST":
       password=request.POST.get('txt_oldpass')
       newpassword=request.POST.get('txt_newpass')
       retypepassword=request.POST.get('txt_pass')
       dbpass=cdsdata.cds_password
       if dbpass == password:
        if newpassword == retypepassword:
            cdsdata.cds_password = newpassword
            cdsdata.save()
            return render(request,'CDS/MyProfile.html',{'msg':"Updated"})
        else:
            return render(request,'CDS/ChangePassword.html',{'msg':"Confirm Password Mismatched"})

       else:
        return render(request,'CDS/ChangePassword.html',{'msg':"Old Password Incorrect"})
    else:
        return render(request,'CDS/ChangePassword.html')

def ADSRegistration(request):
    cds_id = request.session.get('cdsid')

    cds = tbl_cds.objects.get(id=cds_id)

    ward = cds.authorityward
    authority = ward.authority
    place = authority.place   # auto place

    ads_list = tbl_ads.objects.filter(authorityward=ward)

    if request.method == "POST":
        name = request.POST.get('txt_name')
        email = request.POST.get('txt_email')
        contact = request.POST.get('txt_num')
        password = request.POST.get('txt_pass')
        photo = request.FILES.get('file_photo')
        localplace_id = request.POST.get('sel_localplace')

        localplace = tbl_localplace.objects.get(id=localplace_id)

        tbl_ads.objects.create(
            ads_name=name,
            ads_email=email,
            ads_contact=contact,
            ads_password=password,
            ads_photo=photo,
            authorityward=ward,
            localplace=localplace
        )
        return redirect('CDS:ADSRegistration')

    return render(request, 'CDS/ADSRegistration.html', {
        'ads_list': ads_list,
        'place': place
    })


def DeleteADS(request, id):
    cds = tbl_ads.objects.get(id=id)
    cds.delete()
    return redirect('CDS:ADSRegistration')

def ViewKudumbasree(request):
    cds_id = request.session.get('cdsid')

    cds = tbl_cds.objects.get(id=cds_id)

    # Get all kudumbasree under same ward
    kudumbasree_list = tbl_kudumbasree.objects.filter(
        authorityward=cds.authorityward
    )

    return render(request, 'CDS/ViewKudumbasree.html', {
        'kudumbasree_list': kudumbasree_list
    })

def ApproveKudumbasree(request, id):
    data = tbl_kudumbasree.objects.get(id=id)
    data.kudumbasree_status = 1
    data.save()
    return redirect('CDS:ViewKudumbasree')


def RejectKudumbasree(request, id):
    data = tbl_kudumbasree.objects.get(id=id)
    data.kudumbasree_status = 2
    data.save()
    return redirect('CDS:ViewKudumbasree')

def Notification(request):
    cds_id = request.session.get('cdsid')

    cds = tbl_cds.objects.get(id=cds_id)

    notifications = tbl_notification.objects.filter(cds=cds).order_by('-id')

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
            cds=cds   # ✅ only CDS field filled
        )

        return redirect('CDS:Notification')

    return render(request, 'CDS/Notification.html', {
        'notifications': notifications
    })


def DeleteNotification(request, id):
    tbl_notification.objects.get(id=id).delete()
    return redirect('CDS:Notification')

def ViewAuthorityNotification(request):
    cds_id = request.session.get('cdsid')

    cds = tbl_cds.objects.select_related('authorityward__authority').get(id=cds_id)

    # ✅ Get notifications from corresponding authority
    notifications = tbl_notification.objects.filter(
        authority=cds.authorityward.authority
    ).order_by('-id')

    return render(request, 'CDS/ViewAuthorityNotification.html', {
        'notifications': notifications
    })

def CompleteNotification(request, id):
    notification = tbl_notification.objects.get(id=id)
    notification.notification_status = 1   # ✅ Mark as completed
    notification.save()
    return redirect('CDS:Notification')

def logout(request):
    del request.session['cdsid']
    return redirect("Guest:Login")