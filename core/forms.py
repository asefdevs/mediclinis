from django import forms
from core.models import Contact,Appointment,Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('name','email','number','comment')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control' ,'placeholder': 'Your Name',}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Your Email',}),
            'number':forms.TextInput(attrs={'class':'form-control','placeholder': 'Your Number',}),
            'comment':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Your Comment'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'doctor', 'email', 'date', 'time', 'problem',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Problem'}),
            'date':forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder':'date'}),
            'time':forms.TimeInput(attrs={'type':'time','class': 'form-control', 'placeholder':'time'}),
            'doctor':forms.Select(attrs={'class': 'form-control','placeholder':'doctor'}), 
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4,'class': 'form-control' , 'placeholder': 'Enter your comment'}))
    class Meta:
        model= Comment
        fields=('content',)
