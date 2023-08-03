from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

from .views import *
router = DefaultRouter()

router.register('employee',EmployeeViewSet,basename='employee')
router.register('encodedfaces',EncodedFacesViewSet,basename='encodedfaces')
router.register('attendence',EmployeeAttendacentViewSet,basename='attendence')

urlpatterns = [
    path('test/',test),
    path('', include(router.urls)),
    path('face_recognition/',check_face,name='face_recognition'),
    path('update_face_encoding/',update_new_encoding_data,name='update_face_encoding'),
    path('last_update/',last_attendence,name='last_update'),
    path('getEmployee/',employee_details)
    
]

