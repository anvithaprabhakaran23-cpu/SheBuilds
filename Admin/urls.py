from django.urls import path,include
from Admin import views
app_name="Admin"
urlpatterns = [
    path('District/',views.District,name='District'),
    path('deldistrict/<int:did>',views.deldistrict,name='deldistrict'),
    path('editdistrict/<int:eid>',views.editdistrict,name='editdistrict'),
    path('Category/',views.Category,name='Category'),
    path('delcategory/<int:cid>',views.delcategory,name='delcategory'),
    path('editcategory/<int:mid>',views.editcategory,name='editcategory'),
    path('AdminRegistration/',views.AdminRegistration,name='AdminRegistration'),
    path('deladmin/<int:aid>',views.deladmin,name='deladmin'),
    path('editadmin/<int:kid>',views.editadmin,name='editadmin'),
    path('Place/',views.Place,name='Place'),
    path('delplace/<int:did>',views.delplace,name='delplace'),
    path('editplace/<int:eid>',views.editplace,name='editplace'),
    path('Subcategory/',views.Subcategory,name='Subcategory'),
    path('delsubcategory/<int:did>',views.delsubcategory,name='delsubcategory'),
    path('editsubcategory/<int:eid>',views.editsubcategory,name='editsubcategory'),
    path('HomePage/',views.HomePage,name='HomePage'),
    path('UserList/',views.UserList,name='UserList'),
    path('acceptuserlist/<int:aid>',views.Acceptuserlist,name='Accept'),
    path('rejectuserlist/<int:rid>',views.rejectuserlist,name='Reject'),
    path('Reply/<int:id>',views.Reply,name='Reply'),
    path('ViewComplaint/',views.ViewComplaint,name='ViewComplaint'),
    path('ViewFeedback/',views.ViewFeedback,name='ViewFeedback'),
    path('LocalPlace/',views.LocalPlace,name='LocalPlace'),
    path('dellocalplace/<int:did>',views.dellocalplace,name='dellocalplace'),
    path('Ward/',views.Ward,name='Ward'),
    path('delward/<int:did>',views.delward,name='delward'),
    path('AuthorityType/',views.AuthorityType,name='AuthorityType'),
    path('delauthority/<int:did>',views.delauthority,name='delauthority'),
    path('editauthority/<int:eid>',views.editauthority,name='editauthority'),

    path('logout/', views.logout, name='logout'),


]