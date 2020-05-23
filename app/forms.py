from django import forms
from django.contrib.auth.models import User
from .models import Student, Teacher,Classroom,Subject,ClassMember,Timetable
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
User = get_user_model()

class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #interests = forms.ModelMultipleChoiceField(
        #queryset=Subject.objects.all(), 
        #widget=forms.CheckboxSelectMultiple,
        #required=True)
    #interests= forms.ChoiceField(required=True, widget=forms.RadioSelect(
        #attrs={'class': 'Radio'}))

    class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2','is_student']



    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        #Student.interests.add(*self.cleaned_data.get('interests'))
        #Student.interests = self.cleaned_data.get('interests')
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =  '__all__'
        exclude =('password', )

class TeacherRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #interests = forms.ModelMultipleChoiceField(
        #queryset=Subject.objects.all(),
        #widget=forms.CheckboxSelectMultiple,
        #required=True
    #)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_teacher']

    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        #Teacher.interests.add(*self.cleaned_data.get('interests'))

        return user

class ClassroomForm(forms.ModelForm):

    class Meta:
        model = Classroom
        fields = ['classname', 'class_incharge']

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['classname','subject_name']


class ClassMemberForm(forms.ModelForm):

    class Meta:
        model = ClassMember
        fields = ['username','member_id','classname','subject','is_student','is_teacher']
        
class TimetableForm(forms.ModelForm):

    class Meta:
        model = Timetable
        fields = ['classname','subject_name','day','start_at','ends_at']

