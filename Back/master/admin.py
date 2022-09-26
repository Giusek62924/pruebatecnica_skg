from django.contrib import admin
from master.models import *

@admin.register(ENTITY)
class EntityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(CITY)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(ROLE)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']