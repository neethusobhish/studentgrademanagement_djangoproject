from django.urls import path
from .views import *

urlpatterns = [
    path('student_details',students_detailpage)
]