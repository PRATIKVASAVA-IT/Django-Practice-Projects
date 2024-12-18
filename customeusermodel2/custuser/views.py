from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
import requests
from .models import mycustomeuser,trackermodel
from .forms import UserCreationForm,registration_form_user,trackerform
from django.db.models import Sum,Min,Max
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
class userregister(CreateView):
    model=mycustomeuser
    form_class=registration_form_user
    template_name='custuser/user_registration.html'
    success_url='/success/'


class successview(TemplateView):
    template_name='custuser/success.html'    


class trackerview(CreateView,ListView):
    model =trackermodel
    form_class = trackerform
    template_name = 'custuser/tracker4.html'
    success_url='/tracker/'  # Redirect after creating an entry
    

    def get_queryset(self):
        # Define the queryset for ListVie
        
        #return trackermodel.objects.all()
        a1= trackermodel.objects.filter(user=self.request.user)
        a2= trackermodel.objects.filter(user=self.request.user).aggregate(total_amount=Sum('amount'))
        a3=trackermodel.objects.filter(user=self.request.user,amount__gte=0).aggregate(total_amount=Sum('amount'))
        a4=trackermodel.objects.filter(user=self.request.user,amount__lt=0).aggregate(total_amount=Sum('amount'))
        return [a1,a2,a3,a4]
   
    def get_context_data(self, **kwargs
                         
                         ):
         
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()[0]  # List of all records
        #context['Total']=trackermodel.objects.filter(user=self.request.user).aggregate(sum(self.amount))
      
        context['form'] = self.get_form()  # Form for creating new record
       # aggregate_data1 = trackermodel.objects.filter(user=self.request.user).aggregate(total_amount=Sum('amount'))
        #aggregate_data2 = trackermodel.objects.filter(user=self.request.user).aggregate(total_amount=Sum('amount').filter(amount__gte=0))
        #aggregate_data3 = trackermodel.objects.filter(user=self.request.user).aggregate(total_amount=Sum('amount').filter(amount__lt=0))
        context['total']=self.get_queryset()[1]['total_amount']
        #context['expense']=aggregate_data3['total_amount']
        context['Creadited']=self.get_queryset()[2]['total_amount']
        context['expense']=self.get_queryset()[3]['total_amount']
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    