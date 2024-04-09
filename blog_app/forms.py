
from django import forms
from django.core.validators import ValidationError
from .models import Messagee


# class CountactUsForm(forms.Form):
    
#     BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
#     FAVARIT_COLOR_CHOECES=[
        
#         ('blue', 'Blue'),
#         ('green', 'Green'),
#         ('red', 'Red'),
#     ]
#     number=forms.IntegerField(label='number')
  
#     name=forms.CharField(max_length=10, label='yourname')
#     text = forms.CharField(max_length=10, label='your message')
#     birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={'class': 'form-control'}))
    
#     coloers=forms.ChoiceField(choices=FAVARIT_COLOR_CHOECES)
    
   
     
     
     
#      # def clean(self):
#      #    name = self.cleaned_data.get('name')
#      #    text = self.cleaned_data.get('text')
#      #    if name == text :
#      #        raise ValidationError('name and text are same', code='name_text_same')
#     def clean(self):   #زمانی می خواهیم بدانیم که فرم is_validاست این متد کال می شود 
#         name = self.cleaned_data.get('name')      #می خواهیم بدانیم نیم و تکست مثله هم هستند یا نه 
#         text = self.cleaned_data.get('text')
#         if name == text :
#             raise ValidationError('name and text are same', code='name_text_same')
    
    
        
#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if 'a' in name:
#             raise ValidationError('a shod not in name', code='a_in_name')
        # return name
    
    
class MessageeForm(forms.ModelForm):
        class Meta:
                model = Messagee
                fields ='__all__'
                widgets={
                        
                        'title': forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'enter your title',
                                'style': 'max-width: 400px;'
                        }),
                        'text': forms.Textarea(attrs={
                                'class': 'form-control',
                                'placeholder': 'enter your text',
                                'style': 'max-width: 400px;'
                                
                        }),
                       
                                                      
                         'email': forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'enter your email',
                                'style': 'max-width: 400px;'
                        }),
                        'age':forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'enter your age',
                                'style': 'max-width: 400px;'
                        }),
                        'data':forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'enter your data',
                                'style': 'max-width: 400px;'
                        })
                }
               
#     title = forms.CharField(max_length=50)
#     text = forms.CharField(widget=forms.Textarea())
#     email = forms.EmailField(widget=forms.EmailInput())
    
   
        
    
      
     
    
       