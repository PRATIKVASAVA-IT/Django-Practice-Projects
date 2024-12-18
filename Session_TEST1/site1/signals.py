from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from django.http import request
from django.contrib.auth.models import User

@receiver(user_logged_in,sender=User)
def user_session_sigal(sender,request,user,**kwargs):
    request.session['user']=200
    
    print('yaha Tak to aya tha!')

@receiver(user_logged_out,sender=User)
def user_session_sigal2(sender,request,user,**kwargs):
    request.session.flush()
    
    print('yaha Tak se aya tha!')