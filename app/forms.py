from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField , PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'each-form-input-inner'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'each-form-input-inner'}))
    email = forms.CharField( required=True, widget=forms.EmailInput(attrs={'class':'each-form-input-inner'}))
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'each-form-input-inner'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'each-form-input-inner'}))            
    password = forms.CharField(label=_("Password"),strip=False,
               widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'each-form-input-inner'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old Password"),
    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'each-form-input-inner'}))
    new_password1=forms.CharField(label=_("New Password"),
    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'each-form-input-inner'}), help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_("Confirm New Password"),
    strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'each-form-input-inner'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'each-form-input-inner'}),
        'locality':forms.TextInput(attrs={'class':'each-form-input-inner'}),
        'city':forms.TextInput(attrs={'class':'each-form-input-inner'}),
        'state':forms.Select(attrs={'class':'each-form-input-inner'}),
        'zipcode':forms.NumberInput(attrs={'class':'each-form-input-inner'})}

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'each-form-input-inner'})
    )