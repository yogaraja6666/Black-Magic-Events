from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from app.models import User, Profile
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password','id':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password','id':'password2'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class EditUserProfileForm(UserChangeForm):
    password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email']


class PasswordChangeingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Enter Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'password1','placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'password2','placeholder':'Confirm New Password'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']