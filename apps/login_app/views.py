from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)


def signin(request):
	return render(request, 'login_app/signin.html')

def signup(request):
	return render(request, 'login_app/signup.html')

def register(request):
	results = User.objects.registerVal(request.POST)
	if results['status'] == True:
		user = User.objects.createUser(request.POST)
		messages.success(request, 'User was created. Please log in.')
	else: 
		genErrors(request, results['errors'])
	return redirect('/')

def login(request):
	results =User.objects.loginVal(request.POST)
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/')

	request.session['first_name'] = results['user'][0].first_name
	request.session['last_name'] = results['user'][0].last_name
	request.session['email'] = results['user'][0].email
	request.session['user_id'] = results['user'][0].id
	request.session['user_rights'] = results['user'][0].user_rights
	request.session['company_name'] = results['user'][0].company.company_name
	return redirect('/')

def logout(request):
	request.session.flush()
	return redirect('/')
	


