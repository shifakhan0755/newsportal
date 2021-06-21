from django import forms
from .models import ContactModel,EntertainmentModel,StateModel,CoronaModel,CareerModel,IPLModel,WorldModel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserCreationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields ='__all__'

class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class': 'form-control'}),
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class tagForm(forms.ModelForm):
    class Meta:
        model=EntertainmentModel
        fields = '__all__'

class tagstateForm(forms.ModelForm):
    class Meta:
        model=StateModel
        fields = '__all__'

class tagcoronaForm(forms.ModelForm):
    class Meta:
        model = CoronaModel
        fields = '__all__'

class tagcareerForm(forms.ModelForm):
    class Meta:
        model = CareerModel
        fields = '__all__'

class tagiplForm(forms.ModelForm):
    class Meta:
        model = IPLModel
        fields = '__all__'

class tagworldForm(forms.ModelForm):
    class Meta:
        model = WorldModel
        fields = '__all__'





