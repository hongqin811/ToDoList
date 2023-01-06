from django.shortcuts import render, get_object_or_404, redirect
# from django.conf import settings
from django.http import HttpResponse
from .models import Member, Work, Action
from .forms import MemberForm, WorkForm, CreateUserForm, ActionForm, PasswordChangingForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from datetime import date
import calendar 
from calendar import HTMLCalendar

from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, "index.html",{})

@login_required(login_url='/login')
def home_view(request):
	user = request.user
	qlist = Action.objects.filter(user__id=user.id)
	today = date.today()
	calendar = HTMLCalendar().formatmonth(today.year, today.month)
	context = {'user':user, 'qlist':qlist, 'year': today.year, 'month': today.month, 'day':today.day, 'calendar':calendar}

	return render(request, "home.html", context)

def member_view(request):
	obj = Member.objects.all()
	context = {"obj": obj}
	return render(request, "member.html", context)

def register_view(request):
	if request.user.is_authenticated:
		messages.error(request, 'You have been logged in.')
		return redirect('/')
	form = CreateUserForm(request.POST or None)
	if form.is_valid():
		form.save()
		user = form.cleaned_data.get('username')
		messages.success(request, 'Hi ' + user + '! Your account has been successfully registered')
		return redirect('/login')

	context = {
		'form':form
		}
	context = {'form':form}
	return render(request, "register.html", context)

def login_view(request):
	if request.user.is_authenticated:
		messages.error(request, 'You have been logged in.')
		return redirect('/')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'Login success')
			return redirect('/')
		else:
			messages.info(request, 'Username or Password is incorrect')
			return render(request, "login.html", {})
	return render(request, "login.html", {})

def logout_view(request):
	logout(request)
	messages.success(request, 'Logout success')
	return redirect('/login')

@login_required(login_url='/login')
def changepw_view(request):
	if request.method == 'POST':
		form = PasswordChangingForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('/changepw')
		else:
			messages.error(request, 'Please correct the error below.')
			return redirect('/changepw')
	else:
		form = PasswordChangingForm(request.user)

	# if request.method == 'POST':
	# 	form = PasswordChangingForm(request.user, request.POST)
	# 	if form.is_valid():
	# 		user = form.save()
	# 		update_session_auth_hash(request, user)
	# 		messages.success(request, 'Your password was successfully updated!')
	# 		return redirect('changepw_view')
	# 	else:
	# 		messages.error(request, 'Please correct the error below.')
	# else:
	# 	form = PasswordChangingForm(request.user)

		return render(request, 'changepw.html', {'form': form})


def personal_view(request, member_id):
	obj = Member.objects.get(id=member_id)
	qlist = Work.objects.filter(member__id=member_id)
	context = {"obj":obj, "qlist":qlist}
	return render(request, "personal.html", context)

def addWork_view(request, member_id):
	obj = Member.objects.get(id=member_id)
	form = WorkForm(request.POST or None)
	if form.is_valid():
		temp = form.save(commit=False)
		temp.member = obj
		temp.save()
		form = WorkForm()
	context = {'form':form, "obj":obj}
	return render(request, "addWork.html", context)

@login_required(login_url='/login')
def addAction_view(request):
	user = request.user
	form = ActionForm(request.POST or None)
	if form.is_valid():
		temp = form.save(commit=False)
		temp.user = user
		temp.save()
		messages.success(request, "New action added!!")
		return redirect('home_view')
	context = {'form':form, "user":user}
	return render(request, "addAction.html", context)

def edit_list_view(request, list_id):
	item = Action.objects.get(id=list_id)
	form = ActionForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		# this is ur job

		return redirect('home_view')
	return render(request, "edit_list.html", {'item':item, 'form':form})

def delete_view(request, list_id):
	item = Action.objects.get(id=list_id)
	item.delete()
	return redirect('home_view')
