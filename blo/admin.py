from django.contrib import admin
from .models import Books
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import UserProfileInfo,User
#admin.site.register(UserProfileInfo)

admin.site.register(Books)
# Register your models here.
'''class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

'''
