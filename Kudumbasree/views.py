from django.shortcuts import render,redirect
from Guest.models import *
from Kudumbasree.models import*
from Authority.models import*
from User.models import*
from datetime import date
from dateutil.relativedelta import relativedelta
import random

# Create your views here.

def HomePage(request):
    return render(request,'Kudumbasree/HomePage.html')
def MyProfile(request):
    kudumbasree=tbl_kudumbasree.objects.get(id=request.session['kid'])
    return render(request,'Kudumbasree/MyProfile.html',{'kudumbasree':kudumbasree})

def EditProfile(request):
    editdata=tbl_kudumbasree.objects.get(id=request.session['kid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_num')
        address=request.POST.get('txt_address')
        editdata.kudumbasree_name=name
        editdata.kudumbasree_email=email
        editdata.kudumbasree_contact=contact
        editdata.kudumbasree_address=address

        editdata.save()
        return render(request,'Kudumbasree/EditProfile.html',{'msg':'Updated'})
    else:
        return render(request,'Kudumbasree/EditProfile.html',{'editdata':editdata})

    return render(request,'Kudumbasree/EditProfile.html')

def ChangePassword(request):
    userdata=tbl_kudumbasree.objects.get(id=request.session['kid'])
    if request.method=="POST":
       password=request.POST.get('txt_oldpass')
       newpassword=request.POST.get('txt_newpass')
       retypepassword=request.POST.get('txt_pass')
       dbpass=userdata.kudumbasree_password
       if dbpass == password:
        if newpassword == retypepassword:
            userdata.kudumbasree_password = newpassword
            userdata.save()
            return render(request,'Kudumbasree/MyProfile.html',{'msg':"Updated"})
        else:
            return render(request,'Kudumbasree/ChangePassword.html',{'msg':" Password Mismatched"})

       else:
        return render(request,'Kudumbasree/ChangePassword.html',{'msg':"Enter Correct Password"})
    else:
        return render(request,'Kudumbasree/ChangePassword.html')

def Meeting(request):
    kudu=tbl_kudumbasree.objects.get(id=request.session['kid'])
    meeting=tbl_meeting.objects.filter(kudumbasree=request.session['kid'])
    if request.method=="POST":
        details=request.POST.get('txt_details')
       
        time=request.POST.get('time')
        Todate=request.POST.get('todate')
        loc=request.POST.get('txt_loc')
        url=request.POST.get('txt_url')
        tbl_meeting.objects.create(meeting_details=details,kudumbasree=kudu,meeting_time=time,meeting_todate=Todate,meeting_location=loc,meeting_url=url)
        return render(request,'Kudumbasree/Meeting.html',{'msg':'Inserted'})
    else:
        return render(request,'Kudumbasree/Meeting.html',{'meeting':meeting})

def  deletemeeting(request,did):
        tbl_meeting.objects.get(id=did).delete()
        return render(request,'Kudumbasree/Meeting.html',{'msg':'Deleted'})
def  Addattendance(request,did):
     tbl_meeting.objects.get(id=did)
     return render(request,'Kudumbasree/Meeting.html',{'msg':'Attendance'})
def MyMembers(request):
    kudu=tbl_kudumbasree.objects.get(id=request.session['kid'])
    Members=tbl_members.objects.filter(kudumbasree=kudu,members_status=1)
    return render(request,'Kudumbasree/MyMembers.html',{'Members':Members})
def deletemembers(request,did):
        tbl_members.objects.get(id=did).delete()
        return render(request,'Kudumbasree/MyMembers.html',{'msg':'Deleted'})

def AddNotification(request):
    notification=tbl_notification.objects.filter(kudumbasree=request.session['kid'])

    if request.method=="POST":
        details=request.POST.get('txt_details')
        loc=request.POST.get('txt_loc')
        title=request.POST.get('txt_title')
        files=request.FILES.get('file_photo')
        tbl_notification.objects.create(notification_details=details,notification_location=loc,notification_title=title,notification_file=files,kudumbasree=tbl_kudumbasree.objects.get(id=request.session['kid']))
        return render(request,'Kudumbasree/AddNotification.html',{'msg':'Inserted'})
    else:
        return render(request,'Kudumbasree/AddNotification.html',{'notification':notification})

def deletenotification(request,did):
        tbl_notification.objects.get(id=did).delete()
        return render(request,'Kudumbasree/AddNotification.html',{'msg':'Deleted'})

def  editnotification(request,eid):
    edit=tbl_notification.objects.get(id=eid)
    edit.notification_status=1
    edit.save()
    return render(request,'Kudumbasree/AddNotification.html',{'msg':'Updated'})

def ViewUsers(request):
    users=tbl_user.objects.all()
    return render(request,'Kudumbasree/ViewUsers.html',{'users':users})

def  deleteUsers(request,did):
        tbl_members.objects.get(id=did).delete()
        return render(request,'Kudumbasree/ViewUsers.html',{'msg':'Deleted'})

def AddProduct(request):
    kudu=tbl_kudumbasree.objects.get(id=request.session['kid'])
    category=tbl_category.objects.all()
    product=tbl_product.objects.filter(kudumbasree=request.session['kid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        photo=request.FILES.get('file_photo')
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        price=request.POST.get('txt_price')
        tbl_product.objects.create(product_name=name,kudumbasree=kudu,product_details=details,product_file=photo,category=category,product_price=price)
        return render(request,'Kudumbasree/AddProduct.html',{'msg':'Inserted'})
    else:
        return render(request,'Kudumbasree/AddProduct.html',{'product':product,'category':category})

def MyProduct(request):
    product=tbl_product.objects.filter(kudumbasree=request.session['kid'])
    return render(request,'Kudumbasree/MyProduct.html',{'product':product})
def AddStock(request,pid):
    product=tbl_product.objects.get(id=pid)
    if request.method == 'POST':
        stock=request.POST.get('txt_stock')
        tbl_stock.objects.create(stock_count=stock,product=product)
        return render(request,'Kudumbasree/AddStock.html',{'msg':'Inserted'})
    else:
        return render(request,'Kudumbasree/AddStock.html')
def AddGallery(request,pid):
    product=tbl_product.objects.get(id=pid)
    if request.method == 'POST':
        photo=request.FILES.get('file_photo')
        tbl_gallery.objects.create(product=product,gallery_photo=photo)
        return render(request,'Kudumbasree/AddGallery.html',{'msg':'Inserted'})
    else:
        return render(request,'Kudumbasree/AddGallery.html')
def ViewMembersRqst(request):
    users = tbl_members.objects.filter(
        kudumbasree=request.session['kid'],
        members_status=0
    )
    return render(request,'Kudumbasree/ViewMembersRqst.html',{'users':users})
def Accept(request, did):
    # uid = tbl_user id you are trying to add
    Members=tbl_members.objects.get(id=did)
    acc_members = tbl_members.objects.filter(user=Members.user,members_status=1).count()
    print(acc_members)
    if acc_members>0:
        return render(request, "Kudumbasree/ViewMembersRqst.html",{"msg": "This user already belongs to another Kudumbasree"})
    else:
        Members.members_status=1
        Members.save()
        return render(request, "Kudumbasree/ViewMembersRqst.html",{"msg": "Member Accepted"})
def Reject(request,rid):
    Members=tbl_members.objects.get(id=rid)
    Members.members_status=2
    Members.save()
    return render(request,'Kudumbasree/ViewMembersRqst.html',{'msg':"Member Rejected"})
def Attendance(request,mid):
    members=tbl_members.objects.filter(kudumbasree=request.session['kid'])
    for i in members:
        i.status = tbl_attendance.objects.filter(member=i.id,meeting=mid).values_list('attendance_status', flat=True).first()
        savings = tbl_saving.objects.filter(member=i.id).order_by('-id').first()
        if savings:
            diff = relativedelta(date.today(), savings.saving_date)
            i.amount = int(diff.months) * 500
        else:
            i.amount = 500
        i.paymentstatus = tbl_saving.objects.filter(saving_date__month=date.today().month).count()
    return render(request,'Kudumbasree/Attendance.html',{'user':members,"mid":mid})

def addsavings(request, mid, amount, mtID):
    tbl_saving.objects.create(
        member = tbl_members.objects.get(id=mid),
        saving_amount=amount
    )
    return redirect("Kudumbasree:Attendance",mtID)

def Present(request,did,mid):

    tbl_attendance.objects.create(
        attendance_status = 1,
        meeting = tbl_meeting.objects.get(id=mid),
        member = tbl_members.objects.get(id=did)
    )
    return redirect("Kudumbasree:Attendance",mid)
def Absent(request,aid,mid):
    attendence = tbl_attendance.objects.create(
        attendance_status = 2,
        meeting = tbl_meeting.objects.get(id=mid),
        member = tbl_members.objects.get(id=aid)
    )
    tbl_fine.objects.create(
        fine_amount = 50,
        member = tbl_members.objects.get(id=aid)
    )
    return redirect("Kudumbasree:Attendance",mid)

def viewfinelist(request):
    fine = tbl_fine.objects.filter(member__kudumbasree=request.session['kid'])
    return render(request,"Kudumbasree/ViewFineList.html",{"fine":fine})

def ViewBooking(request):
    booking = tbl_booking.objects.filter(tbl_cart__product__kudumbasree=request.session['kid'],booking_status__gt=0)
    return render(request,'Kudumbasree/ViewBooking.html',{"booking":booking})
def UpdateCartStatus(request, cid, status):
    cart = tbl_cart.objects.get(id=cid)
    cart.cart_status = status
    cart.save()
    booking = cart.booking
    total_items = tbl_cart.objects.filter(booking=booking).count()
    delivered_items = tbl_cart.objects.filter(booking=booking,cart_status=6).count()
    if total_items == delivered_items:
        booking.booking_status = 3
        booking.save()
    return redirect("Kudumbasree:ViewBooking")
def logout(request):
    del request.session['kid']
    return redirect("Guest:Login")

def AddChit(request):
    kudu=tbl_kudumbasree.objects.get(id=request.session['kid'])
    chit = tbl_chit.objects.filter(kudumbasree=request.session['kid'])
    members = tbl_members.objects.filter(kudumbasree=request.session['kid'])
    if request.method=="POST":
        total=request.POST.get('txt_total') 
        perhead=request.POST.get('txt_perhead')
        chit = tbl_chit.objects.create(chit_totalamount=total,chit_amount=perhead,kudumbasree=kudu)
        for i in members:
            tbl_chitmembers.objects.create(
                member = tbl_members.objects.get(id=i.id),
                chit = tbl_chit.objects.get(id=chit.id)
            )
        return render(request,'Kudumbasree/AddChit.html',{'msg':'Inserted'})
    else:
         return render(request,'Kudumbasree/AddChit.html',{'chit':kudu,"chitdata":chit})
    
def deletechit(request,did):
        tbl_chit.objects.get(id=did).delete()
        return render(request,'Kudumbasree/AddChit.html',{'msg':'Deleted'})

def selectchit(request, id):
    chitmember = tbl_chitmembers.objects.filter(chit=id,chitmembers_status=1)
    if request.method == "POST":
        chitmem_count = tbl_chitmembers.objects.filter(chitmembers_date__month=date.today().month).count()
        if chitmem_count > 0:
            return render(request,"Kudumbasree/SelectChit.html",{"msg":"Already Loted in this month"})
        member_ids = tbl_chitmembers.objects.filter(chitmembers_status=0,chit=id).values_list('id', flat=True)
        if member_ids:
            random_member = random.choice(member_ids)
            tbl_chitmembers.objects.filter(id=random_member).update(chitmembers_date=date.today(),chitmembers_status=1)
            return render(request, "Kudumbasree/SelectChit.html",{"msg":"User Selected.."})
        else:
            return render(request, "Kudumbasree/SelectChit.html",{"msg":"No More User For Selection"})
    return render(request, "Kudumbasree/SelectChit.html",{"members":chitmember})

def ViewNotification(request):
    kud_id = request.session.get('kid')

    kud = tbl_kudumbasree.objects.select_related(
        'authorityward__authority', 'localplace'
    ).get(id=kud_id)

    # ✅ Authority Notifications
    authority_notifications = tbl_notification.objects.filter(
        authority=kud.authorityward.authority
    ).order_by('-id')

    # ✅ CDS Notifications (same ward)
    cds = tbl_cds.objects.filter(authorityward=kud.authorityward).first()
    cds_notifications = tbl_notification.objects.filter(
        cds=cds
    ).order_by('-id')

    # ✅ ADS Notifications (same localplace)
    ads_notifications = tbl_notification.objects.filter(
        ads__localplace=kud.localplace
    ).order_by('-id')

    return render(request, 'Kudumbasree/ViewNotification.html', {
        'authority_notifications': authority_notifications,
        'cds_notifications': cds_notifications,
        'ads_notifications': ads_notifications
    })