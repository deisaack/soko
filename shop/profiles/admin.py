from __future__ import unicode_literals
from django.contrib import admin
from authtools.admin import NamedUserAdmin
from .models import Profile
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile


class NewUserAdmin(NamedUserAdmin):
    inlines = [UserProfileInline]
    list_display = ('is_active', 'email', 'name',
                    'is_superuser', 'is_staff',)

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
