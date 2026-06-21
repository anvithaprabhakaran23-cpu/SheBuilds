from django.urls import path
from ADS import views
app_name = "ADS"

urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),

    path('viewkudumbasree/', views.ViewKudumbasree, name='ViewKudumbasree'),

    path('notification/', views.Notification, name='Notification'),
    path('deletenotification/<int:id>/', views.DeleteNotification, name='DeleteNotification'),

    path('viewnotification/', views.ViewNotification, name='ViewNotification'),
    path('completenotification/<int:id>/', views.CompleteNotification, name='CompleteNotification'),


    path('logout/', views.logout, name='logout'),
]