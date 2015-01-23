from django import forms  
from django.contrib.auth.models import User  

class LoginForm(forms.Form):  
    username = forms.CharField(  
        required=True,  
#        label=u"username",  
        error_messages={'required': 'please enter your name'},  
        widget=forms.TextInput(  
            attrs={  
                'class':'form-control',
                'type':'email',
                'id':'inputEmail3',
                'placeholder':'Email',
                'name':'username',
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
#        label=u"pwd",  
        error_messages={'required': u'please enter your password'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"password",  
                'type':'password',
                'class':'form-control',
                'id':'inputPassword3',
                'name':'password',
            }  
        ),  
    )     
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"gun")  
        else:  
            cleaned_data = super(LoginForm, self).clean()
