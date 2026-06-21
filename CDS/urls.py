from django.urls import path
from CDS import views
app_name = "CDS"

urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),

    path('ads/', views.ADSRegistration, name='ADSRegistration'),
    path('deleteads/<int:id>/', views.DeleteADS, name='DeleteADS'),

    path('viewkudumbasree/', views.ViewKudumbasree, name='ViewKudumbasree'),
    path('approvekudumbasree/<int:id>/', views.ApproveKudumbasree, name='ApproveKudumbasree'),
    path('rejectkudumbasree/<int:id>/', views.RejectKudumbasree, name='RejectKudumbasree'),

    path('notification/', views.Notification, name='Notification'),
    path('deletenotification/<int:id>/', views.DeleteNotification, name='DeleteNotification'),

    path('viewauthoritynotification/', views.ViewAuthorityNotification, name='ViewAuthorityNotification'),
    path('completenotification/<int:id>/', views.CompleteNotification, name='CompleteNotification'),

    path('logout/',views.logout,name='logout'),

]