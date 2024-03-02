from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('signup/',views.user_sign_up,name="signup"),
    path('logout/',views.user_logout , name ='logout'),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('doctors/',views.doctors,name="doctors"),
    path('booking/',views.booking,name="booking"),
    path('contact/',views.contact,name="contact"),
    path("departments/",views.departments,name="departments"),
]