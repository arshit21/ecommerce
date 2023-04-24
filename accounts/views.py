from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User, Customer, Vendor

def register_customer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        address_line_1 = request.POST['address_line_1']
        address_line_2 = request.POST['address_line_2']
        city = request.POST['city']
        state = request.POST['state']

        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is already taken')
                return redirect('register_customer')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register_customer')
                else:
                    #looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name,
                                                    is_customer=True)
                    user.save()
                    customer = Customer.objects.create(user_id=user.id,username=username, password=password, email=email, first_name=first_name, last_name=last_name, address_line_1=address_line_1, address_line_2=address_line_2, city=city, state=state)
                    customer.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register_customer')
    else:
        return render(request, 'accounts/register_customer.html')

def register_vendor(request):
    if request.method == 'POST':
        #Get form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is already taken')
                return redirect('register_vendor')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register_vendor')
                else:
                    #looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, is_vendor=True)
                    user.save()
                    vendor = Vendor.objects.create(user_id=user.id,username=username, email=email, first_name=first_name, last_name=last_name,)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register_vendor')
    else:
        return render(request, 'accounts/register_vendor.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)


        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def customer_dashboard(request):
    current_user = request.user
    customer = Customer.objects.filter(username=current_user.username)
    context = {
        'customer': customer
    }
    return render(request, 'accounts/customer_dashboard.html', context)

def vendor_dashboard(request):
    return render(request, 'accounts/vendor_dashboard.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
