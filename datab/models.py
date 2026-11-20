from django.db import models
from django.utils.text import slugify

# Create your models here.

class Student(models.Model):

    user_gender = [
        ("male", "MALE"),
        ("female","FMALE")
    ]

    roll_no = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(null=True,max_length=20,choices=user_gender)
    dob = models.DateField(null=True)
    class_name = models.IntegerField(default=10)
    phone_no = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(default='unknown',blank=True)
    slug = models.SlugField(null=True,blank = True)
    created = models.DateField(null=True,auto_now_add=True)
    updated = models.DateField(null=True,auto_now=True)
    photo = models.ImageField(upload_to='photos',null=True)

    def save(self):
        self.slug = slugify(self.address)
        super().save()

    def __str__(self):
        return self.first_name

class Grade(models.Model):
    student_name = models.OneToOneField(Student,on_delete=models.CASCADE,null=True)
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    computer = models.IntegerField()
    total = models.IntegerField(blank=True,null=True)
    average = models.FloatField(blank=True,null=True)
    grade = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.student_name.first_name+' '+self.student_name.last_name 