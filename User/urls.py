from django.urls import path,include
from User import views
app_name="User"
urlpatterns = [
    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('Complaint/',views.Complaint,name='Complaint'),
    path('deletecomplaint/<int:did>',views.deletecomplaint,name='deletecomplaint'),
    path('Feedback/',views.Feedback,name='Feedback'),
    path('kudumbam/',views.kudumbam,name='kudumbam'),
    path('requesttojoin/<int:kid>',views.requesttojoin,name='requesttojoin'),
    path('ViewNotification/',views.ViewNotification,name='ViewNotification'),
    path('ViewProduct/',views.ViewProduct,name='ViewProduct'),
    path("addcart/<int:id>",views.addcart,name="addcart"),
    path('MyCart/', views.MyCart, name='MyCart'),
    path('DelCart/<int:did>/', views.DelCart, name='DelCart'),
    path('CartQty/', views.CartQty, name='CartQty'),
    path('viewfine/', views.viewfine, name='viewfine'),

    path('payment/', views.payment, name='payment'),
    path('finepayment/<int:id>', views.finepayment, name='finepayment'),
    path('loader/', views.loader, name='loader'),
    path('paymentsuc/', views.paymentsuc, name='paymentsuc'),
    path('MyBooking/',views.MyBooking,name='MyBooking'),
    path('MyKudumbasree/',views.MyKudumbasree,name='MyKudumbasree'),
    path('ViewMeeting/<int:id>',views.ViewMeeting,name='ViewMeeting'),
    path('MySavings/',views.MySavings,name='MySavings'),
    path('addsavings/<int:id>/<int:amount>',views.addsavings,name='addsavings'),

    
    path('viewlot/<int:id>',views.viewlot,name='viewlot'),
    path('logout',views.logout,name='logout'),


]
