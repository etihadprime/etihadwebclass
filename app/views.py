from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.messages.views import SuccessMessageMixin
from .forms import TeacherRegisterForm,StudentRegisterForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.mixins import  LoginRequiredMixin
from .models import Subject,Classroom,ClassMember,Timetable,Chat
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView
)

def index(request):
    return render(request, 'index.html')


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def studentregister(request):   
        form1 = StudentRegisterForm(request.POST or None)

        if form1.is_valid():
            user = form1.save()
            user.is_student = True
            user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return HttpResponseRedirect('/')
    
        form1 = StudentRegisterForm()
        context={
        'form1' : form1
        }
        return render(request,'registration/student.html',context)

def teacherregister(request):   
        form1 = TeacherRegisterForm(request.POST or None)
        if form1.is_valid():
            user = form1.save()
            user.is_teacher = True
            user.save()

            return HttpResponseRedirect('/')
    
        form1 = TeacherRegisterForm()
        context={
        'form1' : form1
        }
        return render(request,'registration/teacher.html',context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, f'Welcome To your Account')
                print("login successful")
                return HttpResponseRedirect('/')

            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})

def logout(request):
    auth.logout(request)
    #del request.session['username']
    return HttpResponseRedirect("/")

def ClassroomList(request):
    context = {
        'classrooms' : Classroom.objects.all(),
        'classmembers'    : ClassMember.objects.all(),
        'schedules'  : Timetable.objects.all().order_by('start_at'),
        'subs'       : Subject.objects.all()
        }
    return render(request,'app/classroom_list.html',context)


class ClassroomListView(LoginRequiredMixin,ListView):
    model = Classroom
    context_object_name = 'classrooms'
    template_name = "app/classroom_list.html"
    

class ClassroomDetailView(LoginRequiredMixin,DetailView):
    model = Classroom

class ClassroomCreateView(LoginRequiredMixin,CreateView):
    model = Classroom
    fields = ['classname','class_incharge']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class ClassroomUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/classroom_update_form.html"
    model = Classroom
    fields = ['classname','class_incharge']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ClassroomVerifyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'app/classroom_verify_form.html'
    model = Classroom
    fields = ['verified']


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ClassroomDeleteView(LoginRequiredMixin,DeleteView):
    model = Classroom
    success_url = '/classroom_list'

    def test_func(self):
        Classroom = self.get_object()
        if self.request.user == Classroom.username:
            return True
        return False


def SubjectList(request):
    context = {
        'subjects' : Subject.objects.all()
        }
    return render(request,'app/subject_list.html',context)


class SubjectListView(LoginRequiredMixin,ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = "app/subject_list.html"
    

class SubjectDetailView(LoginRequiredMixin,DetailView):
    model = Subject

class SubjectCreateView(LoginRequiredMixin,CreateView):
    model = Subject
    fields = ['classname','subject_name']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/subject_update_form.html"
    model = Subject
    fields = ['classname','subject_name']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class SubjectVerifyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'app/subject_verify_form.html'
    model = Subject
    fields = ['verified']


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class SubjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Subject
    success_url = '/subject_list'

    def test_func(self):
        Subject = self.get_object()
        if self.request.user == Subject.username:
            return True
        return False


def ClassMemberList(request):
    context = {
        'classmembers' : ClassMember.objects.all()
        }
    return render(request,'app/classmember_list.html',context)


class ClassMemberListView(LoginRequiredMixin,ListView):
    model = ClassMember
    context_object_name = 'classmembers'
    template_name = "app/classmember_list.html"
    

class ClassMemberDetailView(LoginRequiredMixin,DetailView):
    model = ClassMember

class ClassMemberCreateView(LoginRequiredMixin,CreateView):
    model = ClassMember
    fields = ['username','member_id','classname','subject','is_student','is_teacher']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class ClassMemberUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/classmember_update_form.html"
    model = ClassMember
    fields = ['username','member_id','classname','subject','is_student','is_teacher']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ClassMemberVerifyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'app/classmember_verify_form.html'
    model = ClassMember
    fields = ['verified']


    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ClassMemberDeleteView(LoginRequiredMixin,DeleteView):
    model = ClassMember
    success_url = '/classmember_list'

    def test_func(self):
        ClassMember = self.get_object()
        if self.request.user == ClassMember.username:
            return True
        return False


def TimetableList(request):
    context = {
        'timetables' : Timetable.objects.all().order_by('start_at')
        }
    return render(request,'app/timetable_list.html',context)


class TimetableListView(LoginRequiredMixin,ListView):
    model = Timetable
    context_object_name = 'timetables'
    template_name = "app/timetable_list.html"
    

class TimetableDetailView(LoginRequiredMixin,DetailView):
    model = Timetable

class TimetableCreateView(LoginRequiredMixin,CreateView):
    model = Timetable
    fields = ['classname','subject_name','day','start_at','ends_at']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)



class TimetableUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/timetable_update_form.html"
    model = Timetable
    fields = ['classname','subject_name','day','start_at','ends_at']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class TimetableDeleteView(LoginRequiredMixin,DeleteView):
    model = Timetable
    success_url = '/timetable_list'

    def test_func(self):
        Timetable = self.get_object()
        if self.request.user == Timetable.username:
            return True
        return False


def chatroom(request):
    if request.method == "POST":
        classname = request.POST['classname']
        user_name = request.POST['user_name']
        message = request.POST['message']

        Chat.objects.create(
            classname = classname,
            user_name = user_name,
            message = message
        )        
    
    return HttpResponse('')

class CrudView(ListView):
    model = Chat
    template_name = 'app/classroom_detail.html'
    context_object_name = 'chats'