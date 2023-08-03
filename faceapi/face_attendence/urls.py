from django.urls import path
from .views import *

urlpatterns = [
    path('register/',faceapp),
    path('markattendence/',mark_attendence)
]
