from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Mata(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields