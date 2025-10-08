from django.contrib import admin
from .models import Event, Signup

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'signup_enabled')
    search_fields = ('title',)
    list_filter = ('signup_enabled',)

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('event',)

# Customize the admin site titles
admin.site.site_header = "Temple Management Admin"
admin.site.site_title = "Temple Website"
admin.site.index_title = "Welcome to the CK Temple Admin Dashboard"
def each_context(self, request):
        context = super().each_context(request)
        context['extra_css'] = [staticfiles_storage.url('css/admin_custom.css')]
        return context