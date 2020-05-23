# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import receiver
from datetime import datetime
from django.urls import reverse
from django.utils.timezone import now

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    """Student models"""
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    # interests = models.OneToOneField(Subject, related_name='mentees', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    """Teacher models"""
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    # interests = models.OneToOneField(Subject, related_name='mentors', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username

class Classroom(models.Model):
    classname      = models.CharField(max_length=100,primary_key=True)
    class_incharge  = models.CharField(max_length=100, null=True)

    objects         = models.Manager()

    def __str__(self):
        return self.classname
    
    def get_absolute_url(self):
        return reverse("classroom-detail", kwargs={"pk": self.classname})

class Subject(models.Model):
    classname        = models.ForeignKey(Classroom, related_name="Subject1", on_delete=models.CASCADE)
    subject_name     = models.CharField(max_length=100, null=True)
    #subject_incharge = models.CharField(max_length=100, null=True)

    objects         = models.Manager()


    def get_absolute_url(self):
        return reverse("subject-detail", kwargs={"pk": self.pk})
    
    

class ClassMember(models.Model):
    username   = models.CharField(max_length=50,primary_key=True)
    member_id  = models.CharField(max_length=16, null=True)
    classname  = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subject    = models.CharField(max_length=30)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects         = models.Manager()

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("classmember-detail", kwargs={"pk": self.username})

    
class Timetable(models.Model):
    classname        = models.CharField(max_length=100, null=True)
    subject_name     = models.CharField(max_length=100, null=True)
    day              = models.CharField(max_length=15, null=True)
    start_at         = models.TimeField()
    ends_at          = models.TimeField()
    #subject_incharge = models.CharField(max_length=100, null=True)

    objects         = models.Manager()
    
    def get_absolute_url(self):
        return reverse("timetable-detail", kwargs={"pk": self.pk})


class Chat(models.Model):
    classname        = models.CharField(max_length=100, null=True)
    user_name        = models.CharField(max_length=100, null=True)
    message          = models.TextField(max_length=300, null=True)
    send_at          = models.DateTimeField(auto_now_add=True)

    objects         = models.Manager()
