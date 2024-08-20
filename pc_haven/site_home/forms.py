from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username","password2" ]


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]
