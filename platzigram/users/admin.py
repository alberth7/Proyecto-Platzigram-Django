# from django
from django.contrib.auth.admin import UserAdmin as BaseUseAdmin
from django.contrib import admin
from django.contrib.auth.models import User

# Models
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
#admin.site.register(Profile)
    '''Profile admin.'''
    list_display = ('pk','user','phone_number', 'website', 'picture') 
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website')
    search_fields = (
        'user__email', 
        'user__first_name', 
        'user__last_name',
        'phone_number'
        )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )
    fieldsets = (
        ('Profile',{
            'fields':(
                ('user','picture'),
            ),
         
        }),
        ('Extra info',{
            'fields':(
                ('phone_number','website'),
                ('biography'),
            ),
        }),
        ('Metadata',{
            'fields':(
                ('created'),
                ('modified'),
            )
        }),
    )

    readonly_fields = ('created','modified','user')
    

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'  

class UserAdmin(BaseUseAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)