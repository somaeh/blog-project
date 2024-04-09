from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input100', 'style': 'max-width 300px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'enter your email'}))
    
    
    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username', password=self.cleaned_data.get('password')))
        if user is not None:
            return self.cleaned_data.get('password')
        else:
            raise ValidationError('not croct', code='password')

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('first_name', 'last_name', 'email')
    
    
            
    