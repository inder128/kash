from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages


def register(request):
	if(request.method == "POST"):
		username = request.POST['username']
		password = request.POST['password']
		user = User.objects.create_user(username=username, password=password)
		user.save()
		messages.success(request, "Successfuly registered!!! Welcome "+username)
		return redirect('/')
	return render(request, 'register.html')


def login(request):
	if(request.method == "POST"):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			messages.success(request, "Successfuly logged in!!! Welcome "+username)
			return redirect('/')
		else:
			messages.error(request, "No user with these credentials in our Database")
	return render(request, 'login.html')


def logout(request):
	auth_logout(request)
	messages.success(request, "Successfuly logged out!!!")
	return redirect('/')



