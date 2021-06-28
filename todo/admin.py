from django.contrib import admin

from .models import Todo
from todo.models import UserProfileInfo

admin.site.register(Todo)
admin.site.register(UserProfileInfo)
