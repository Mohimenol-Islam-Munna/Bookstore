from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin 
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    model = get_user_model()

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username']


admin.site.register(get_user_model(), CustomUserAdmin)

