
global l1
l1=[]

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

    # Render the control page for GET requests
    fm=clinet_data.objects.all().order_by('-id')[:5]
    return render (request,'main/controlpage.html',{'fm':fm})