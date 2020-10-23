from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    #paths for employee site
    path('employee/<str:email>',views.employee,name='employee'),
    path('employee/edit/<str:email>',views.edit,name='edit'),
    #paths for admin site
     path('hr_admin/',views.admin,name='admin'),
    path('hr_admin/delete/<str:email>',views.delete,name='delete'),
    path('hr_admin/new/',views.create,name='create_new'),
]
