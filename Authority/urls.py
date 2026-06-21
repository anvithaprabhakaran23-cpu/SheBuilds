from django.urls import path,include
from Authority import views
app_name="Authority"
urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('ajaxplace',views.ajaxplace,name='ajaxplace'),
    path('ajaxlocalplace/',views.ajaxlocalplace,name='ajaxlocalplace'),
    path('MyWard/',views.MyWard,name='MyWard'),
    path('deletemyward/<int:did>',views.deletemyward,name='deletemyward'),

    path('cds/', views.CDSRegistration, name='CDSRegistration'),
    path('deletecds/<int:id>/', views.DeleteCDS, name='DeleteCDS'),

    path('notification/', views.Notification, name='Notification'),
    path('deletenotification/<int:id>/', views.DeleteNotification, name='DeleteNotification'),

    path('completenotification/<int:id>/', views.CompleteNotification, name='CompleteNotification'),

    path('logout/', views.logout, name='logout'),

]
   

