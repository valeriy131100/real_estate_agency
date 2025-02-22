from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnershipInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = ['new_building']
    list_filter = [
        'new_building',
        'rooms_number',
        'has_balcony',
        'active'
    ]
    raw_id_fields = ['liked_by']
    inlines = [OwnershipInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    list_display = [
        'full_name',
        'phone',
        'pure_phone'
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
