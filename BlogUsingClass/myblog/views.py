from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.views.generic import TemplateView,RedirectView
import requests
from .forms import user_registrationForm,blog_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Blog
from django.contrib import messages
import json


# Create your views here.
def base(request):
    return render(request,'myblog/base.html')
def home(request):
    return render(request,'myblog/home.html')

class UserRegistrationCreateView(CreateView):
    model=User
    form_class=user_registrationForm
    template_name='myblog/registration.html'
    success_url='/success/'

class successView(TemplateView):    
    template_name='myblog/success.html'

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class dashboardView(TemplateView):    
    template_name='myblog/dashboard.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Instantiate the BlogListView object
        blog_list_view = BlogListView()

        # Set up the request object (important for CBVs to function correctly)
        blog_list_view.request = self.request

        # Fetch the blog queryset
        blog_list_view.object_list = blog_list_view.get_queryset()

        # Pass the queryset (or whatever data you need) to the dashboard context
        context["prv"] = blog_list_view.object_list
        return context
@method_decorator(login_required(login_url='/login/'),name='dispatch')
class BlogView(CreateView):
    model=Blog
    form_class=blog_form
    template_name='myblog/blog.html'
    success_url='/'
    
     
    
        
    
        
class BlogListView(ListView):
    model=Blog
    template_name='myblog/home.html'
    context_object_name='object'
    queryset = Blog.objects.all().order_by('-date')
    
        

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class PostDetailView(DetailView):
    model=Blog
    template_name='myblog/postview.html'
    context_object_name='object'

@method_decorator(login_required(login_url='/login/'),name='dispatch')
class UpdateBlogView(UpdateView):
    model=Blog
    fields='__all__'
    template_name='myblog/Updateblogview.html'
    success_url='/success/'

    
class SearchListView(ListView):
    model=Blog
    template_name='myblog/home.html'
    context_object_name='object'
    
    def get_queryset(self,*args):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        print(query)
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset
        
class myDeleteview(DeleteView):    
    model=Blog
    success_url='/'
    template_name='myblog/mydeleteconfirm.html'

def apidata(request):
    import requests
from django.shortcuts import render
from django.http import JsonResponse
import logging

# Set up logging for debugging purposes
logger = logging.getLogger(__name__)

def apidata(request):
    url = 'http://127.0.0.1:8000/studentapi/'

    try:
        # Send the GET request to the API
        response = requests.get(url=url)
        
        # Raise an exception for HTTP error codes (like 4xx, 5xx)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Render the data to the template
        return render(request, 'myblog/apidata.html', {'data': data})
    
    except requests.exceptions.RequestException as e:
        # Log the exact error for debugging
        logger.error(f"Error fetching API data: {e}")
        
        # Optionally, provide feedback to the user (you can customize this)
        return JsonResponse({'error': 'Unable to fetch data from the API.'}, status=500)

    
    '''
     try:
         url='http://127.0.0.1:8000/studentapi/'
         r=requests.get(url=url)
         data=r.json()
         return render (request,'myblog/apidata.html',{'data':data})
     except:
         print('Somthing Wrong')
'''



        