from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('my-login/',views.my_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.my_logout,name='logout'),
    path('create-record',views.create_record,name='createrecord'),
    path('view/<int:id>/',views.view_record,name='view_record'),
]