# users/views.py
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.urls import reverse_lazy
from django.views import generic
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)
        field_classes = {'email': EmailField}

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"