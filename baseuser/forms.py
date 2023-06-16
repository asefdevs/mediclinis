from django import forms
from .models import User

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'password')
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}),
            'password': forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}),
        }


     

            
        
class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'re-password'}))
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name',  'password','confirm_password')
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'last_name'}),
            # 'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}),
            'password': forms.TextInput(attrs={'class':'form-control', 'placeholder':'password'}),
            'confirm_password': forms.TextInput(attrs={'class':'form-control', 'placeholder':'repassword'}),
        }


    def clean(self):
        cleaned_data= super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password!=confirm_password:
            raise forms.ValidationError('passwords dont match')
    
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('username already exists')
        return  username
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password)<8:
            raise forms.ValidationError('password is too short')
        return password
