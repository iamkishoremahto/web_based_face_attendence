from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class EncodedFacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = EncodedFaces
        fields = '__all__'

class EmployeeAttendenceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = EmployeeAttendence
        fields = '__all__'

        # fields = ['id', 'employee', 'employeeid', 'attendence_date', 'last_update']

    
