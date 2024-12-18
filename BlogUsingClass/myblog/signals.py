from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import login
from django.dispatch import receiver
from django.utils import timezone


@receiver(user_logged_in)
def create_session_on_login(sender, request, user, **kwargs):
    # Set a session variable when the user logs in
    request.session['last_login'] = str(timezone.now())
    request.session['user_id'] = user.id
    
    # Any other session data you want to store
    print(f"Session created for user {user.username} at {timezone.now()}")


