from django.db import models
import os
# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(max_length=200)
    employee_name = models.CharField(max_length=200)
    employee_email = models.EmailField()
    employee_mobile = models.CharField(max_length=15)
    employee_photo = models.TextField()
    employee_designation = models.CharField(max_length=100)
    employee_address = models.TextField()
    last_updated = models.DateTimeField(auto_now= True)

class EmployeeAttendence(models.Model):
    
    employee_id = models.CharField(max_length=100)
    attendence_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

   

class LeaveType(models.Model):
    leave_type = models.CharField(max_length=60)
    last_update = models.DateTimeField(auto_now=True)

class EncodedFaces(models.Model):
    encoded_faces = models.JSONField()

class Leave(models.Model):
    employee_id = models.ForeignKey(
        Employee,on_delete= models.CASCADE,
        related_name='employeeId'
    )
    leave_start_date = models.DateField(auto_now_add=True)
    leave_end_date = models.DateField(auto_now_add=True)
    total_leaves = models.IntegerField()
    leave_reasons = models.TextField()
    leave_type = models.ForeignKey(
        LeaveType,on_delete= models.CASCADE,
        related_name='leaveType'
    )

    last_update = models.DateTimeField(auto_now=True)


