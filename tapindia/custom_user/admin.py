from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import EmailUserChangeForm, EmailUserCreationForm
from custom_user.models import EmailUser



class EmailUserAdmin(UserAdmin):

    """EmailUser Admin model."""

    fieldsets = (
        (None, {'fields': ('email', 'password', 'Label')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'Label')
        }
    ),
    )

    # The forms to add and change user instances
    form = EmailUserChangeForm
    add_form = EmailUserCreationForm
	
    def assign_group(self, email, password, **extra_fields):
        form = EmailUserCreationForm(data=request.POST)
        if form.is_valid():
                user = self.model(email=email, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
                user_type = form.cleaned_data['Label']
                if user_type == 'Truck':
                    g1 = Group.objects.get(name=Truck)
                    g1.user_set.add(TRUCK_USER)
                    user_group.save()
                    user.save(using=self._db)
                    return user
                elif user_type == 'Company':
                    g2 = Group.objects.get(name=Company)
                    g2.user_set.add(COMPANY_USER)
                    user_group.save()
                    user.save(using=self._db)
                    return user

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'Label')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions', )

# Register the new EmailUserAdmin
admin.site.register(EmailUser, EmailUserAdmin)


