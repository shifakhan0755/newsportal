from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
from home.models import CareerModel,EntertainmentModel,WorldModel,IPLModel,StateModel,CoronaModel
from .models import Main
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    class Meta:
        model = CareerModel
        fields = "__all__"

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']

class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['last_login','is_superuser','groups','user_permissions','username','first_name','last_name','email','is_staff','is_active','date_joined']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'date_joined': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'last_login': forms.TextInput(attrs={'class': 'form-control'}),
                   'user_permissions': forms.Select(attrs={'class': 'form-control'}),
                  # 'password':forms.PasswordInput(attrs={'class': 'form-control'}),
                   'groups':forms.Select(attrs={'class': 'form-control'}),

                   }

class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields ='__all__'
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }

class UserForm(UserCreationForm):
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

class EntertainmentForm(forms.ModelForm):
    class Meta:
        model = EntertainmentModel
        fields = '__all__'
        exclude = {'slug':'slug','s_vedio':'s_vedio','a':'a'}
        labels = {'d_description':'Detail description','s_image':'Image'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
                   'caption': forms.TextInput(attrs={'class': 'form-control','placeholder':'Caption'}),
                   'd_description': RichTextField(),
                   'description': RichTextField(),
                   'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag'}),
                   'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'select'}),

                   }

class CareerForm(forms.ModelForm):
    class Meta:
        model = CareerModel
        fields = '__all__'
        exclude = {'slug':'slug','s_vedio':'s_vedio','a':'a'}
        labels = {'detail_description':'Detail description','s_image':'Image'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
                   'caption': forms.TextInput(attrs={'class': 'form-control','placeholder':'Caption'}),
                   'detail_description': RichTextField(),
                   'description': RichTextField(),
                   'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag'}),
                   'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'select'}),

                   }
class CoronaForm(forms.ModelForm):
    class Meta:
        model = CoronaModel
        fields = '__all__'
        exclude = {'slug':'slug','s_vedio':'s_vedio','a':'a'}
        labels = {'d_description':'Detail description','s_image':'Image'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
                   'caption': forms.TextInput(attrs={'class': 'form-control','placeholder':'Caption'}),
                   'd_description': RichTextField(),
                   'description': RichTextField(),
                   'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag'}),
                   'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'select'}),

                   }

class WorldForm(forms.ModelForm):
    class Meta:
        model = WorldModel
        fields = '__all__'
        exclude = {'slug':'slug','s_vedio':'s_vedio','a':'a'}
        labels = {'detail_description':'Detail description','s_image':'Image'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
                   'caption': forms.TextInput(attrs={'class': 'form-control','placeholder':'Caption'}),
                   'detail_description': RichTextField(),
                   'description': RichTextField(),
                   'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag'}),


                   }

class IPLForm(forms.ModelForm):
    class Meta:
        model = IPLModel
        fields = '__all__'
        exclude = {'slug':'slug','s_vedio':'s_vedio','a':'a'}
        labels = {'detail_description':'Detail description','s_image':'Image'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
                   'caption': forms.TextInput(attrs={'class': 'form-control','placeholder':'Caption'}),
                   'detail_description': RichTextField(),
                   'description': RichTextField(),
                   'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag'}),


                   }

class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = '__all__'
        exclude = {'slug':'slug','s_vedio':'s_vedio','a':'a'}
        labels = {'detail_description':'Detail description','s_image':'Image'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Title'}),
                   'caption': forms.TextInput(attrs={'class': 'form-control','placeholder':'Caption'}),
                   'detail_description': RichTextField(),
                   'description': RichTextField(),
                   'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag'}),
                   'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'select'}),

                   }


