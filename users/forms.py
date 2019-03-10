from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=15, required=True)
	last_name = forms.CharField(max_length=15, required=True) 
	email =forms.EmailField(required=True)
	id_number = forms.CharField(max_length=6, required=True)
	phone_number = forms.CharField(max_length=10, required=True)

	class Meta:
		model=User
		fields=['username', 'first_name', 'last_name', 'email', 'id_number', 'phone_number', 'password1', 'password2']