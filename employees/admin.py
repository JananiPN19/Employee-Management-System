from django.contrib import admin

from .models import Employee,AvailableJob
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_id','phone_num']

@admin.register(AvailableJob)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['job_name']
