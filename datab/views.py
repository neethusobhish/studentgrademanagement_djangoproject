from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm,GradeForm




# Create your views here.

def student_results_page(request):
    results = Student.objects.all()
    return render(request,'results.html',{'results':results})

def studentinformationpage(request,sid):
    stu = Student.objects.get(id = sid)
    return render(request,'stu_info.html',{'sinfo':stu})

def addstudentpage(request):
    if request.method=='POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(student_results_page)
    else:
        form = StudentForm()
    # print('hellooooooooooo')
    # form = StudentForm()
    return render(request,'stu.html',{'form':form})

def editsturesultpage(request,sid):
    stu_result = Student.objects.get(id=sid)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=stu_result)
        if form.is_valid():
            form.save()
            return redirect(student_results_page)
    else:
        form = StudentForm(instance=stu_result)

    return render(request,'result_edit.html',{'form':form})

def DeleteStureultpage(request,sid):
    stu_result = Student.objects.get(id=sid)
    if request.method =='POST':
        stu_result.delete()
        return redirect(student_results_page) 
    return render(request,"delsturesults.html",{'stu_result':stu_result})


def addgradepage(request):
    form = GradeForm()
    return render(request,"addgrade.html",{'form':form})