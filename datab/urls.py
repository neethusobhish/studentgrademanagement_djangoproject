from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("all_student_results",student_results_page,name='all_student_results'),
    path("student_information/<int:sid>",studentinformationpage,name='student_info'),
    path("add_student",addstudentpage,name='addstudent'),
    path("addgrade",addgradepage),
    path("Edit_student_results/<int:sid>",editsturesultpage,name='stu_result_edit'),
    path("Delete_student_results/<int:sid>",DeleteStureultpage,name='stu_result_delete')
    
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)