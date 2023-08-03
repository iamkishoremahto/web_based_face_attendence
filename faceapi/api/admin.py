from django.contrib import admin
from django.apps import apps
from .models import *
# Register your models here.

app_models = apps.get_models()

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id','employee_name','employee_email','employee_mobile','employee_designation','last_updated']

@admin.register(EmployeeAttendence)
class EmployeeAttendenceAdmin(admin.ModelAdmin):
    list_display = ['employee_id','attendence_date','last_update']
# for model in app_models:
#     if not admin.site.is_registered(model):
#         admin.site.register(model)

