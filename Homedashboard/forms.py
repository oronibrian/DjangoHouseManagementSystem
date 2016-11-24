from django import forms
from django.contrib.auth import authenticate,login,logout,get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('User does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('User no longer active')
        return super(UserLoginForm,self,*args,**kwargs).clean()


