from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Question, Answer, Favorite


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username", ]


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Favorite)
