from .models import Subject,ClassMember,Timetable,Classroom,Chat
 
def classdata(request):
     
    classdatas = ClassMember.objects.all()
    subs = Subject.objects.all()
    schedule = Timetable.objects.all().order_by('start_at')
    chats     = Chat.objects.all().order_by('send_at')
    
    return {'classdatas' : classdatas , 'subs' :subs ,'schedule': schedule ,'chats': chats}