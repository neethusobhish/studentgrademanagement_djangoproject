from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def students_detailpage(request):
    return HttpResponse('this is students detail page')
