from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class CustomCreationUserForm(UserCreationForm):

  class Meta:
      model = CustomUser
      fields = [
          'username',
          'email',
          'password1',
          'password2',
          'phone_number',
          'avatar'
      ]

  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      # Username
      self.fields['username'].widget.attrs.update(
        {
          'class' : 'form-control',
          'placeholder': 'Username'
        }
      )
      self.fields['username']
      
      # Email
      self.fields['email'].widget.attrs.update(
        {
          'class' : 'form-control',
          'placeholder' : 'Valid Email'
        }
      )
      self.fields['email'].required=True
      
      # Password
      self.fields['password1'].widget.attrs.update(
        {
          'class' : 'form-control',
          'placeholder' : 'Strong Password'
        }
      )
      # Password_confirm
      self.fields['password2'].widget.attrs.update(
        {
          'class' : 'form-control',
          'placeholder' : 'Password Confirm'
        }
      )
      self.fields['password2'].label = "Confirm Password"
      
      # Phone Number
      self.fields['phone_number'].widget.attrs.update(
        {
          'class' : 'form-control',
          'placeholder' : 'Number: +00 123456789'
        }
      )
      
      self.fields['avatar'].required=False