from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Question, Answer, Favorite
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username", ]


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
