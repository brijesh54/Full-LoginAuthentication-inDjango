from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.forms import fields
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False,
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),
                                    strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))    


class MypasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=500, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False,
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),
                                    strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords don\'t Match')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')         