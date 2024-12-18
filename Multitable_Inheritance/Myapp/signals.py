from django.db.models.signals import post_save
from .models import customer,Profile
from django.dispatch import receiver

@receiver(post_save,sender=customer)
def add_profile(sender,instance,created,**kwarg):
    if created:
        Profile.objects.create(id=instance.id,add1=instance.add1,add2=instance.add2,city=instance.city,
                               dis=instance.dis,state=instance.state,country=instance.country,
                               name=instance.name,mobile=instance.mobile,email=instance.email

                               
                               )
        print('profile has been created..!')
        
