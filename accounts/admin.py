from django.contrib import admin

from accounts.models import Consumer

# Register your models here.



@admin.register(Consumer)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('email', 'position')
    list_filter = ('email', 'position')
    search_fields = ('email', 'position')
    readonly_fields = ('secret_key',)
