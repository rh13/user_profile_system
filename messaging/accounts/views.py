from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignUpForm, EditBioForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile

# Create your views here.

def index(request):
	return render(request, 'index.html')

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return render(request, 'login.html')
		else:
			return HttpResponse("Username or password incorrect")
	return render(request, 'login.html')

def user_signup(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('login'))
	return render(request, 'signup.html',{'signup_form':form})

@login_required
def user_logout(request):
	logout(request)
	return redirect('login')


@login_required
def bio(request):
    bio = UserProfile.objects.all()
    context = {'bio': bio}
    return render(request, 'profile/bio.html', context)


@login_required
def edit_bio(request):
	form = EditBioForm()
	if request.method == "POST":
		form = EditBioForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('bio')
	else:
		form = EditBioForm(instance=request.user)
	return render(request, 'profile/edit_bio.html', {'form':form} )



@login_required
def change_password(request):
	form = PasswordChangeForm( user=request.user)
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('bio')
		else:
			return HttpResponse("invalid password")
	else:
		form = PasswordChangeForm(user=request.user)
	return render(request, 'profile/edit_bio.html', {'form': form})
