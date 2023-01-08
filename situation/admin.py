from django.contrib import admin

from . import models


@admin.register(models.Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')
