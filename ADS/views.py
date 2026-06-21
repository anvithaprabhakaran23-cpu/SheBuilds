from django.shortcuts import render,redirect
from CDS.models import *
from Guest.models import *
from Kudumbasree.models import *
# Create your views here.

def HomePage(request):
    return render(request,'ADS/HomePage.html')

def MyProfile(request):
    adsdata=tbl_ads.objects.get(id=request.session['adsid'])
    if request.method=="POST":
        adsdata.ads_name=request.POST.get('txt_name')
        adsdata.ads_email=request.POST.get('txt_email')
        adsdata.ads_contact=request.POST.get('txt_num')
        adsdata.save()
        return render(request,'ADS/MyProfile.html',{'msg':'Updated'})
    return render(request,'ADS/MyProfile.html',{'ads':adsdata})

def ChangePassword(request):
    adsdata=tbl_ads.objects.get(id=request.session['adsid'])
    if request.method=="POST":
       password=request.POST.get('txt_oldpass')
       newpassword=request.POST.get('txt_newpass')
       retypepassword=request.POST.get('txt_pass')
       dbpass=adsdata.ads_password
       if dbpass == password:
        if newpassword == retypepassword:
            adsdata.ads_password = newpassword
            adsdata.save()
            return render(request,'ADS/MyProfile.html',{'msg':"Updated"})
        else:
            return render(request,'ADS/ChangePassword.html',{'msg':"Confirm Password Mismatched"})

       else:
        return render(request,'ADS/ChangePassword.html',{'msg':"Old Password Incorrect"})
    else:
        return render(request,'ADS/ChangePassword.html')
    
def ViewKudumbasree(request):
    ads_id = request.session.get('adsid')

    if not ads_id:
        return redirect('Guest:Login')

    ads = tbl_ads.objects.select_related('authorityward__authority', 'localplace').get(id=ads_id)

    # ✅ Filter by BOTH localplace + authority
    kudumbasree_list = tbl_kudumbasree.objects.select_related(
        'localplace', 'authorityward__ward'
    ).filter(
        localplace=ads.localplace,
        authorityward__authority=ads.authorityward.authority
    )

    return render(request, 'ADS/ViewKudumbasree.html', {
        'kudumbasree_list': kudumbasree_list
    })

def Notification(request):
    ads_id = request.session.get('adsid')

    ads = tbl_ads.objects.get(id=ads_id)

    notifications = tbl_notification.objects.filter(ads=ads).order_by('-id')

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
            ads=ads   # ✅ ADS notification
        )

        return redirect('ADS:Notification')

    return render(request, 'ADS/Notification.html', {
        'notifications': notifications
    })


def DeleteNotification(request, id):
    tbl_notification.objects.get(id=id).delete()
    return redirect('ADS:Notification')

def ViewNotification(request):
    ads_id = request.session.get('adsid')

    ads = tbl_ads.objects.select_related('authorityward__authority').get(id=ads_id)

    # ✅ Get CDS under same ward
    cds = tbl_cds.objects.filter(authorityward=ads.authorityward).first()

    # ✅ Separate queries
    authority_notifications = tbl_notification.objects.filter(
        authority=ads.authorityward.authority
    ).order_by('-id')

    cds_notifications = tbl_notification.objects.filter(
        cds=cds
    ).order_by('-id')

    return render(request, 'ADS/ViewNotification.html', {
        'authority_notifications': authority_notifications,
        'cds_notifications': cds_notifications
    })

def CompleteNotification(request, id):
    notification = tbl_notification.objects.get(id=id)
    notification.notification_status = 1   # ✅ Mark as completed
    notification.save()
    return redirect('ADS:Notification')

def logout(request):
    del request.session['adsid']
    return redirect("Guest:Login")