# staff/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class StaffRegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=100, help_text='Required. Enter a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StaffRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Enter a valid email address.')
    name = forms.CharField(max_length=100, required=True, help_text='Required. Enter your full name')
    age = forms.IntegerField(required=True, help_text='Required. Enter your age')
    sex = forms.CharField(max_length=10, required=True, help_text='Required. Enter your gender')
    address = forms.CharField(max_length=200, required=True, help_text='Required. Enter your address')
    branch = forms.CharField(max_length=50, required=True, help_text='Required. Enter your branch')
    department = forms.CharField(max_length=50, required=True, help_text='Required. Enter your department')

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'sex', 'address', 'branch', 'department', 'password1', 'password2']

