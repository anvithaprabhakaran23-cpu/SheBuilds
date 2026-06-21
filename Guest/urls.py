from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns = [
    path('UserRegistration/',views.UserRegistration,name='UserRegistration'),
    path('ajaxplace',views.ajaxplace,name='ajaxplace'),
    path('Login/',views.Login,name='Login'),
    path('Authority/',views.Authority,name='Authority'),
    path('ajaxlocalplace/',views.ajaxlocalplace,name='ajaxlocalplace'),
    path('ajaxauthorityward/',views.ajaxauthorityward,name='ajaxauthorityward'),
    path('ajaxauthority/',views.ajaxauthority,name='ajaxauthority'),
    path('Kudumbasree/',views.Kudumbasree,name='Kudumbasree'),
    path('',views.index,name='index'),
  

]