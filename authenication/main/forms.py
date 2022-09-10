from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

class Signup(UserCreationForm):
    email=forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter eamil'}))
    first_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last Name'}))
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super(Signup,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Enter Username'
        self.fields['username'].label=''

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Enter password'
        self.fields['password1'].label=''


        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Enter Password Again'
        self.fields['password2'].label=''

class EditForm(UserChangeForm):
    password=forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email']

    def __init__(self,*args,**kwargs):
        super(EditForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        

class PasswordChange(PasswordChangeForm):
    class Meta:
        model=User 
        fields=['old_password','new_password1','new_password2']
    def __init__(self,*args,**kwargs):
        super(PasswordChange,self).__init__(*args,**kwargs)
        self.fields['old_password'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['class']='form-control'


    



    



