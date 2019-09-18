from django.contrib import admin

# Register your models here.

from .models import DefaultType, Cust

class DefaultTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)

admin.site.register(DefaultType, DefaultTypeAdmin)