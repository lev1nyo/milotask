from django import forms
from user.models import UserNew


class UserNewForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    birthdate = forms.DateField()

    class Meta:
        model = UserNew
