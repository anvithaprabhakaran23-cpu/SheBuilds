from django.urls import path,include
from Kudumbasree import views
app_name="Kudumbasree"
urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('Meeting/',views.Meeting,name='Meeting'),
    path('deletemeeting/<int:did>',views.deletemeeting,name='deletemeeting'),
    path('MyMembers/',views.MyMembers,name='MyMembers'),
    path('deletemembers/<int:did>',views.deletemembers,name='deletemembers'),
    path('AddNotification/',views.AddNotification,name='AddNotification'),
    path('deletenotification/<int:did>',views.deletenotification,name='deletenotification'),
    path('editnotification/<int:eid>',views.editnotification,name='editnotification'),
    path('ViewUsers/',views.ViewUsers,name='ViewUsers'),
    path('deleteUsers/<int:did>',views.deleteUsers,name='deleteUsers'),
    path('AddProduct/',views.AddProduct,name='AddProduct'),
    path('MyProduct/',views.MyProduct,name='MyProduct'),
    path('AddStock/<int:pid>',views.AddStock,name='AddStock'),
    path('AddGallery/<int:pid>',views.AddGallery,name='AddGallery'),
    path('ViewMembersRqst/',views.ViewMembersRqst,name='ViewMembersRqst'),
    path('Accept/<int:did>',views.Accept,name='Accept'),
    path('Reject/<int:rid>',views.Reject,name='Reject'),
    path('Attendance/<int:mid>',views.Attendance,name='Attendance'),
    path('Present/<int:did>/<int:mid>',views.Present,name='Present'),
    path('Absent/<int:aid>/<int:mid>',views.Absent,name='Absent'),
    
    path('viewfinelist/',views.viewfinelist,name='viewfinelist'),
    path('ViewBooking/',views.ViewBooking,name='ViewBooking'),
    path('addsavings/<int:mid>/<int:amount>/<int:mtID>',views.addsavings,name='addsavings'),
    path('logout',views.logout,name='logout'),

    path('UpdateCartStatus/<int:cid>/<int:status>/',views.UpdateCartStatus,name='UpdateCartStatus'),
    path('AddChit/',views.AddChit,name='AddChit'),
    path('deletechit/<int:did>',views.deletechit,name='deletechit'),
    path('selectchit/<int:id>',views.selectchit,name='selectchit'),

    path('viewnotification/', views.ViewNotification, name='ViewNotification'),
    



]