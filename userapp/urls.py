from django.urls import path
from .import views
urlpatterns = [
    path('',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('view/',views.view,name="view"),
    path('loginredirect/',views.loginredirect,name="loginredirect"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('updateuser/<int:pk>',views.updateuser,name="updateuser"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('detailview/<str:pk>',views.detailview,name="detailview"),
    path('adloginfunc/',views.adloginfunc,name="adloginfunc"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
]
