from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def faceapp(request):
    return render(request, 'registration.html')

def mark_attendence(request):
    return render(request, 'mark_attendence.html')