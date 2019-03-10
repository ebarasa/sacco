from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account Has Been Created! You Are Now Able To Login')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required 
def profile(request):
	return render(request, 'users/profile.html')

@login_required 
def details(request):
	return render(request, 'users/details.html')

@login_required 
def activities(request):
	return render(request, 'users/activities.html')

@login_required 
def report(request):
	return render(request, 'users/report.html')
