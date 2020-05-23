from django.urls import path
from .views import teacherregister,studentregister,login_view,logout
from . import views
from .views import (
ClassroomCreateView,ClassroomListView,ClassroomDetailView,ClassroomUpdateView,ClassroomDeleteView,
SubjectCreateView,SubjectListView,SubjectDetailView,SubjectUpdateView,SubjectDeleteView,
ClassMemberCreateView,ClassMemberListView,ClassMemberDetailView,ClassMemberUpdateView,ClassMemberDeleteView,
TimetableCreateView,TimetableListView,TimetableDetailView,TimetableUpdateView,TimetableDeleteView,CrudView,chatroom
)

urlpatterns = [
                path('', views.index, name='index'),
                path('health', views.health, name='health'),
                path('404', views.handler404, name='404'),
                path('500', views.handler500, name='500'),
                path('signup/teacher', teacherregister,name='register-teacher'),
                path('signup/student', studentregister,name='register-student'),
                path('accounts/login/', login_view, name='login'),
                path('logout/', logout,name='logout'),
                #Classroom
                path('classroom/new', ClassroomCreateView.as_view(),name='classroom-create'),
                path('classroom_list', ClassroomListView.as_view(),name='classroom-list'),
                path('classroom/<str:pk>/', ClassroomDetailView.as_view(),name='classroom-detail'),
                path('classroom/<str:pk>/update', ClassroomUpdateView.as_view(),name='classroom-update'),
                path('classroom/<str:pk>/delete', ClassroomDeleteView.as_view(),name='classroom-delete'),
                #path('Classroom/<int:pk>/image',ChildImageUpdateView.as_view(),name='Classroom-image'),
                #Subject
                path('subject/new', SubjectCreateView.as_view(),name='subject-create'),
                path('subject_list', SubjectListView.as_view(),name='subject-list'),
                path('subject/<int:pk>/', SubjectDetailView.as_view(),name='subject-detail'),
                path('subject/<int:pk>/update', SubjectUpdateView.as_view(),name='subject-update'),
                path('subject/<int:pk>/delete', SubjectDeleteView.as_view(),name='subject-delete'),
                # Class Members
                path('classmember/new', ClassMemberCreateView.as_view(),name='classmember-create'),
                path('classmember_list', ClassMemberListView.as_view(),name='classmember-list'),
                path('classmember/<str:pk>/', ClassMemberDetailView.as_view(),name='classmember-detail'),
                path('classmember/<str:pk>/update', ClassMemberUpdateView.as_view(),name='classmember-update'),
                path('classmember/<str:pk>/delete', ClassMemberDeleteView.as_view(),name='classmember-delete'),
                # TimeTable
                path('timetable/new', TimetableCreateView.as_view(),name='timetable-create'),
                path('timetable_list', TimetableListView.as_view(),name='timetable-list'),
                path('timetable/<int:pk>/', TimetableDetailView.as_view(),name='timetable-detail'),
                path('timetable/<int:pk>/update', TimetableUpdateView.as_view(),name='timetable-update'),
                path('timetable/<int:pk>/delete', TimetableDeleteView.as_view(),name='timetable-delete'),
                # chatroom
                path('chat/new',chatroom,name='chatroom'),
                path('crud/',CrudView.as_view(), name='crud_ajax'),
               
               ]