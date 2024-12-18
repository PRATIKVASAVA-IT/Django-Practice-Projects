from django.shortcuts import render,redirect
from .forms import myuser_form,admin_login_form,client_data_form
from random import randint
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import clinet_data,MyUser


def get_id():
    v=randint(111111111111,999999999999)
    return v
    

# Create your views here.
def index(request):
    fm=admin_login_form()
    return render (request,'main/index.html',context={'fm':fm})
'''
def control_page(request):
    if request.method=='POST':
        cust_id=request.POST.get('userInput')
        print(cust_id)
       
        user=MyUser.objects.filter(customer_id=cust_id)
        query = "SELECT user_id FROM your_app_myuser WHERE customer_id = %s"
        users = MyUser.objects.raw(query, [cust_id])
    
        # Collect user IDs from the result
        user_ids = [user1.user_id for user1 in users]
        

        if user.exists():
            fm=client_data_form()
            return render(request,'main/client_data_form.html',context={'fm':fm,'uid':user_ids})
        
    return render(request,'main/controlpage.html')
'''

global l1



def control_page(request):
    if request.method == 'POST':
        # Get the customer ID from the POST request
        cust_id = request.POST.get('userInput')
        

        # Check if the customer exists using ORM
        user = MyUser.objects.filter(customer_id=cust_id)
        print(f'User is {user}')
        cust_data=user.first()
        if cust_data:
             x=cust_data.first_name + " "+ cust_data.last_name 
        if user.exists():
            # Extract user IDs
            user_ids = list(user.values_list('id', flat=True))

            # Render the form with user IDs
            fm = client_data_form()
            return render(request, 'main/client_data_form.html', context={'fm': fm, 'cust_id':cust_id,'cust_user':x})
        

        else:
            # Handle case where customer does not exist
            messages.warning(request,"No user found with the provided Customer ID.")
            return render(request, 'main/controlpage.html')

    # Render the control page for GET 

    
    
    fm=clinet_data.objects.all().order_by('-id')[:10]
       
  
        
    return render (request,'main/controlpage.html', context={'fm':fm } )
    
    
def regi(request):
    if request.method=='POST':
        fm=myuser_form(request.POST)
        #fm.instance.customer_id=get_id()
        print(fm)

        un=request.POST.get('first_name')

        selected_groups = request.POST.get('groups')
        print('You have selected Group:',selected_groups)
        
        
        
         
             
            
             
            
      
                  
             
             
    

        if selected_groups=='2':
                 try:
                    fm.instance.customer_id=get_id()

                    fm.save(commit=False)
                    messages.info(request,'Client is successfully Saved !')
                    messages.info(request,f'{fm.instance.first_name} your account number is {fm.instance.customer_id}.')
                    
                 except Exception as e:
                          print(e)
                          print('inside 2 ')
                          messages.warning(request,'Complete the Reaming Details. Note : All Fiels are compulsary') 
          
                
        elif selected_groups=='1':
            try:
                fm.instance.is_superuser=True
                fm.save(commit=False)
                messages.info(request,'Admin is successfully Saved !')
            except Exception as e:
                      print('inside 1')
                      messages.warning(request,'Complete the Reaming Details. Note : All Fiels are compulsary') 
            
            
        if fm.is_valid():
            fm.save()
        return redirect('/regi/') 

        
        
        '''
        if selected_groups=='2':
                 fm.instance.customer_id=get_id()
                 if fm.is_valid():
                      fm.save()
                      return redirect('/regi/') 
        else:
            fm.is_superuser=True
            if fm.is_valid():
                 fm.save()
                 return redirect('/regi/') 
            

          '''       

    
                
        
        
    fm=myuser_form()
    
    return render(request,'main/regi.html',context={'fm':fm})

def admin_login(request):
     if request.method=='POST':
         uname=request.POST.get('username')
         passw=request.POST.get('password')
     
         user=authenticate(username=uname,password=passw)    
         if user: 
            login(request,user)
            return redirect('/con/')
         else:
              messages.warning(request,'Username or password is wrong! ') 
              return redirect('/')



def admin_logout(request):
    if request.method=='POST':
        logout(request)
        return redirect(reverse('index'))  # Use reverse for named URLs
    else:
        # Redirect for non-POST requests (or handle differently)
        return redirect(reverse('index'))  # Ensure a valid response for all cases
   
def clientData(request):
    if request.method=='POST':
    
        fm=client_data_form(request.POST)
        cust_id = request.POST.get('cust_id')
        print(cust_id)
        
        if fm.is_valid():
            data=fm.save(commit=False)
            try:
                my_user_instance = MyUser.objects.get(customer_id=cust_id )
                print(my_user_instance)
                data.user = my_user_instance  # Assign the user instance to the foreign key
                data.save()  # Save to the database
                messages.info(request, 'Entry Saved!')
                return redirect(reverse('con'))
            except MyUser.DoesNotExist:
                messages.error(request, "User not found with the given customer ID.")
                f1=True
                return render(request,'main/controlpage.html',context={'f1':f1})
             


     



            
 