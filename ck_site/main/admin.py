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