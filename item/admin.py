from django.contrib import admin

from . import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')


@admin.register(models.Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'brand', 'model')
