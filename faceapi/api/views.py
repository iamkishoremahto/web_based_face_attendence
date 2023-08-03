from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from .face_recoginations import face_recognizer,create_encoded_face_json_file
# Create your views here.

def test(request):
    return JsonResponse({"success": True})

@api_view(['POST'])
def check_face(request):
    if request.method == 'POST': 
        image_url = request.data.get('image_url')
        result = face_recognizer(image_url,request)
        return JsonResponse({"result":result,"status":200})

@api_view(['POST'])
def update_new_encoding_data(request):
    if request.method == 'POST': 
        image_url = request.data.get('employee_photo')
        employee_id = request.data.get('employee_id')
        # print(image_url)
        result = create_encoded_face_json_file(image_url,employee_id,request)
        return JsonResponse({"result":result,"status":200})

@api_view(['POST'])
def last_attendence(request):
    if request.method == 'POST':
        employee_id = request.data.get('employee_id')

        employee_attendance = EmployeeAttendence.objects.filter(employee_id=employee_id).order_by('-id').first()
        serializer = EmployeeAttendenceSerializer(employee_attendance)
        return JsonResponse(serializer.data)

@api_view(['POST'])
def employee_details(request):
    if request.method == 'POST':
        employee_id = request.data.get('employee_id')

        employee_attendance = Employee.objects.filter(employee_id=employee_id).order_by('-id').first()
        serializer = EmployeeSerializer(employee_attendance)
        return JsonResponse(serializer.data)




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EncodedFacesViewSet(viewsets.ModelViewSet):
    queryset = EncodedFaces.objects.all()
    serializer_class = EncodedFacesSerializer

class EmployeeAttendacentViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAttendence.objects.all()
    serializer_class = EmployeeAttendenceSerializer






