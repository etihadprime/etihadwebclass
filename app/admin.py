from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import Teacher,Student
from .models import Subject,Classroom,ClassMember,Timetable,Chat
from django.contrib.auth.models import Group
from .models import User   

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_teacher", "is_student","is_staff",)
    list_display_links = ("username", "email",  "is_teacher", "is_student","is_staff",)
    list_filter = ("username", "is_teacher", "is_student","is_staff",)
    search_fields = ("username",)
    list_per_page = 10

class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(ClassMember)
admin.site.register(Chat)
admin.site.register(Timetable)
admin.site.register(User,CustomUserAdmin)
admin.site.unregister(Group)
