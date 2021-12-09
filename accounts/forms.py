from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import UserBase
class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = UserBase

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display Name'
        self.fields['email'].label='Email Address'
