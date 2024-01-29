from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator
from .models import *
from django.forms import ValidationError
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        return cleaned_data

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        def clean_username(self):
            username = self.cleaned_data['username']

            if len(username) < 5:
                raise forms.ValidationError('Username should be more than 5 letters.')
            
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('This username is already in use.')
            return username
        
        def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('This email address is already registered.')
            
            email_validator = EmailValidator()
            try:
                email_validator(email)
            except ValidationError as e:
                raise ValidationError("Invalid email address. {}".format(e))
            
            return email

        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get('password1')
            password2 = cleaned_data.get('password2')

            if len(password1) < 10 or len(password2) < 10:
                raise forms.ValidationError("Password is too small, it's length should be 10 characters.")

            if password1 and password2 and password1 != password2:
                raise forms.ValidationError('Passwords do not match.')

            if password1:
                digit_count = sum(c.isdigit() for c in password1)
                special_char_count = sum(1 for c in password1 if not c.isalnum())
                
                if digit_count < 2 or special_char_count < 1:
                    raise forms.ValidationError('Password must contain at least 2 numbers and 1 special character.')

            return cleaned_data

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user','profileid')