from django.contrib import admin

from . import models


class AddressCollectionInline(admin.TabularInline):
    model = models.Address
    extra = 1


class ContactCollectionInline(admin.TabularInline):
    model = models.Contact
    extra = 1


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')
    inlines = [AddressCollectionInline, ContactCollectionInline]


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('zipcode', 'address', 'number', 'district', 'city', 'state')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'cell')
