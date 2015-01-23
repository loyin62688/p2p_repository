from django import forms  
from django.contrib.auth.models import User  

class LoginForm(forms.Form):  
    username = forms.CharField(  
        required=True,  
        label=u"username",  
        error_messages={'required': 'please enter your name'},  
        widget=forms.TextInput(  
            attrs={  
                'class':'col-sm-2 control-label',
                'for':'inputEmail3',
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
        label=u"password",  
        error_messages={'required': u'please enter your password'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"password",  
            }  
        ),  
    )     
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"gun")  
        else:  
            cleaned_data = super(LoginForm, self).clean()
