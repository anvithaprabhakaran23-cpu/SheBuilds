from django.shortcuts import render,redirect
from Guest.models import *
from User.models import*
from Kudumbasree.models import*
from django.db.models import Sum
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your views here.
def HomePage(request):
    return render(request,'User/HomePage.html')

def MyProfile(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/MyProfile.html',{'user':userdata})

def EditProfile(request):
    editdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_num')
        address=request.POST.get('txt_address')
        editdata.user_name=name
        editdata.user_email=email
        editdata.user_contact=contact
        editdata.user_address=address

        editdata.save()
        return render(request,'User/EditProfile.html',{'msg':'Updated'})
    else:
        return render(request,'User/EditProfile.html',{'editdata':editdata})

    return render(request,'User/EditProfile.html')

def ChangePassword(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
       password=request.POST.get('txt_oldpass')
       newpassword=request.POST.get('txt_newpass')
       retypepassword=request.POST.get('txt_pass')
       dbpass=userdata.user_password
       if dbpass == password:
        if newpassword == retypepassword:
            userdata.user_password = newpassword
            userdata.save()
            return render(request,'User/MyProfile.html',{'msg':"Updated"})
        else:
            return render(request,'User/ChangePassword.html',{'msg':" Password Mismatched"})

       else:
        return render(request,'User/ChangePassword.html',{'msg':"Enter Correct Password"})
    else:
        return render(request,'User/ChangePassword.html')

def Complaint(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    complaint=tbl_complaint.objects.all()
    if request.method=="POST":
        title=request.POST.get('txt_complaint')
        content=request.POST.get('txt_content')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata)
        return render(request,'User/Complaint.html',{'msg':'Inserted'})
    else:
        return render(request,'User/Complaint.html',{'complaint':complaint})
def  deletecomplaint(request,did):
        tbl_complaint.objects.get(id=did).delete()
        return render(request,'User/Complaint.html',{'msg':'Deleted'})

def Feedback(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    feedback=tbl_feedback.objects.all()
    if request.method=="POST":
        content=request.POST.get('txt_feedback')
        tbl_feedback.objects.create(feedback_content=content,user=userdata)
        return render(request,'User/Feedback.html',{'msg':'Inserted'})
    else:
        return render(request,'User/Feedback.html',{'feedback':feedback})

def kudumbam(request):
    userplace = tbl_user.objects.get(id=request.session['uid'])
    kudumbam=tbl_kudumbasree.objects.filter(localplace=userplace.localplace,authorityward=userplace.authorityward)
    kudumbasree_status=1
    return render(request,'User/ViewKudumbam.html',{"kudumbam":kudumbam})

def requesttojoin(request,kid):
    kudumbam=tbl_kudumbasree.objects.get(id=kid)
    userdata=tbl_user.objects.get(id=request.session['uid'])
    count=tbl_members.objects.filter(user=userdata,kudumbasree=kid).count()
    membercount=tbl_members.objects.filter(kudumbasree=kid).count()
    if membercount < 12:
        if count > 0:
            return render(request,'User/ViewKudumbam.html',{'msg':'already requested'})
        else:
            tbl_members.objects.create(kudumbasree=kudumbam,user=userdata)
            return render(request,'User/ViewKudumbam.html',{'msg':'Inserted'})
    else:
        return render(request,'User/ViewKudumbam.html',{'msg':'Member Count Exedeed....'})


def ViewNotification(request):
    user_id = request.session.get('uid')
    user = tbl_user.objects.select_related(
        'authorityward__authority',
        'localplace'
    ).get(id=user_id)

    # ✅ Authority Notifications
    authority_notifications = tbl_notification.objects.filter(
        authority=user.authorityward.authority,
        notification_status=1
    ).order_by('-id')

    # ✅ CDS Notifications
    cds = tbl_cds.objects.filter(authorityward=user.authorityward).first()
    cds_notifications = tbl_notification.objects.filter(
        cds=cds,
        notification_status=1
    ).order_by('-id')

    # ✅ ADS Notifications
    ads_notifications = tbl_notification.objects.filter(
        ads__localplace=user.localplace,
        notification_status=1
    ).order_by('-id')

    # ✅ Kudumbasree Notifications
    kud = tbl_kudumbasree.objects.filter(
        localplace=user.localplace,
        authorityward=user.authorityward
    ).first()

    usermembercount = tbl_members.objects.filter(user=user_id,members_status=1).count()
    kud_notifications = []
    if usermembercount > 0:
        usermember = tbl_members.objects.get(user=user_id,members_status=1)
        kud_notifications = tbl_notification.objects.filter(
            kudumbasree=usermember.kudumbasree.id,
            notification_status=1
        ).order_by('-id')

    return render(request, 'User/ViewNotification.html', {
        'authority_notifications': authority_notifications,
        'cds_notifications': cds_notifications,
        'ads_notifications': ads_notifications,
        'kud_notifications': kud_notifications
    })

from django.db.models import Sum

def ViewProduct(request):
    product = tbl_product.objects.all()

    for i in product:
        total_stock = tbl_stock.objects.filter(
            product=i.id
        ).aggregate(total=Sum('stock_count'))['total'] or 0

        total_cart = tbl_cart.objects.filter(
            product=i.id,
            cart_status=1
        ).aggregate(total=Sum('cart_quantity'))['total'] or 0

        available_stock = total_stock - total_cart
        i.total_stock = max(0, available_stock)   # prevent negative stock

    return render(request,'User/ViewProduct.html',{'product':product})

def addcart(request, id):
    productdata=tbl_product.objects.get(id=id)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            return render(request,"User/Viewproduct.html",{'msg':"Already added"})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            return render(request,"User/Viewproduct.html",{'msg':"Added To cart"})
    else:
        bookingdata = tbl_booking.objects.create(user=userdata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        return render(request,"User/Viewproduct.html",{'msg':"Added To cart"})
def MyCart(request):
    if request.method=="POST":
        bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_amount=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        cart = tbl_cart.objects.filter(booking=bookingdata)
        for i in cart:
            i.cart_status = 1
            i.save()
        return redirect("User:payment")
    else:
        bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
        if bookcount > 0:
            book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
            request.session["bookingid"] = book.id
            cart = tbl_cart.objects.filter(booking=book)
            for i in cart:
                total_stock = tbl_stock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_count'))['total']
                total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=1).aggregate(total=Sum('cart_quantity'))['total']
                # print(total_stock)
                # print(total_cart)
                if total_stock is None:
                    total_stock = 0
                if total_cart is None:
                    total_cart = 0
                total =  total_stock - total_cart
                i.total_stock = total
            return render(request,"User/MyCart.html",{'cartdata':cart})
        else:
            return render(request,"User/MyCart.html")
   
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:MyCart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_quantity=qty
   cartdata.save()
   return redirect("User:MyCart")

def viewfine(request):
    fine = tbl_fine.objects.filter(member__user=request.session['uid'])
    return render(request,"User/Fine.html",{"fine":fine})

def finepayment(request, id):
    fine = tbl_fine.objects.get(id=id)
    if request.method == "POST":
        fine.fine_status = 1
        fine.save()
        return redirect('User:loader')
    else:
        return render(request,"User/Payment.html",{"amount":fine.fine_amount})
    
def payment(request):
    booking = tbl_booking.objects.get(id=request.session["bookingid"])
    if request.method == "POST":
        booking.booking_status = 2
        booking.save()
        cart = tbl_cart.objects.filter(booking=booking)
        for i in cart:
            i.cart_status = 2
            i.save()
        return redirect('User:loader')
    else:
        return render(request,"User/Payment.html",{"amount":booking.booking_amount})

def loader(request):
    return render(request, "User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Paymentsuc.html")

def MyBooking(request):
    booking = tbl_booking.objects.filter(user=request.session['uid'],booking_status__gt=0)
    return render(request,'User/MyBooking.html',{"bookingdata":booking})

def MyKudumbasree(request):
    member_id = tbl_members.objects.filter(
        user=request.session['uid'],
        members_status=1
    ).values_list("kudumbasree", flat=True).first()
    my_kudumbasree= []
    if member_id:
        my_kudumbasree = tbl_kudumbasree.objects.get(id=member_id)
    return render(request,"User/MyKudumbasree.html",{"kudumbasree":my_kudumbasree})

def ViewMeeting(request, id):
    meeting = tbl_meeting.objects.filter(kudumbasree=id).order_by('meeting_todate')
    member = tbl_members.objects.filter(user=request.session['uid'],kudumbasree=id).first()
    chit = tbl_chit.objects.filter(kudumbasree=id,chit_status=0).first()
    if chit:
        for i in meeting:
            i.status = tbl_attendance.objects.filter(member=member,meeting=i.id).values_list('attendance_status', flat=True).first()
            savings = tbl_saving.objects.filter(member=member.id).order_by('-id').first()
            print(savings) 
            if  savings != None:
                diff = relativedelta(date.today(), savings.saving_date)
                print(diff.months)
                i.amount = int(diff.months) * int(chit.chit_amount)
                print(i.amount)
            else:
                meetingcount = tbl_meeting.objects.filter(meeting_todate__month__lte=date.today().month,kudumbasree=id).count()
                # print(meetingcount)
                i.amount = meetingcount * int(chit.chit_amount)
    return render(request,"User/ViewMeeting.html",{"meeting":meeting})

def MySavings(request):
    savings = tbl_saving.objects.filter(
        member__user=request.session['uid'])
    return render(request,"User/MySavings.html",{"savings":savings})

def addsavings(request, id, amount):
    meeting = tbl_meeting.objects.get(id=id)
    member = tbl_members.objects.filter(user=request.session['uid'],kudumbasree=meeting.kudumbasree.id).first()
    if request.method == "POST":
        tbl_attendance.objects.create(
            attendance_status = 1,
            meeting = tbl_meeting.objects.get(id=id),
            member = tbl_members.objects.get(id=member.id)
        )
        tbl_saving.objects.create(
            member = tbl_members.objects.get(id=member.id),
            saving_amount=amount
        )
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"amount":amount})

def viewlot(request, id):
    chit = tbl_chitmembers.objects.filter(chit__kudumbasree=id,chitmembers_status=1)
    return render(request,"User/ViewLot.html",{"members":chit})

def logout(request):
    del request.session['uid']
    return redirect("Guest:Login")
