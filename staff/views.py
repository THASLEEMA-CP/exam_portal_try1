# staff/views.py
from django.shortcuts import render, redirect
from .forms import StaffRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'staff/home.html')

def register_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("hi")
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = StaffRegistrationForm()
    return render(request, 'staff/register_staff.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page, or a page of your choice
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    # If the request method is not POST or authentication fails, render the login page.
    return render(request, 'staff/login.html')