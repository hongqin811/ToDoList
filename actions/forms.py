from django import forms
from .models import Member, Work, Action
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = [
			'name',
			'dob',
			'gender'
		]

class WorkForm(forms.ModelForm):
	class Meta:
		model = Work
		fields = [
			'description',
			'due'
		]

class ActionForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter description'}))
	class Meta:
		model = Action
		fields = [
			'description',
			'due',
			'finish'
		]

		widgets = {
			'due': forms.TextInput(attrs={'class':'form-control', 'rows': 20, 'cols': 50, 'placeholder':'YYYY-MM-DD'}),
		}

class CreateUserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}

class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

	class Meta:
		model = User
		fields = ['old_password', 'new_password1', 'new_password2']