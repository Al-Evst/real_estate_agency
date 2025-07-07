from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owners.through  
    raw_id_fields = ['owner']
    extra = 1
    verbose_name = 'Собственник'
    verbose_name_plural = 'Собственники'


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owners__full_name', 'owners__pure_phone']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'display_owners']
    list_editable = ['new_building']
    list_filter = ['new_building', 'town', 'active', 'has_balcony', 'rooms_number']
    raw_id_fields = ['likes', 'owners']
    inlines = [OwnersInline]
    exclude = ['owners']  

    def display_owners(self, obj):
        return ", ".join(owner.full_name for owner in obj.owners.all())
    display_owners.short_description = 'Собственники'


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'created_at']
    raw_id_fields = ['user', 'flat']
    search_fields = ['user__username', 'flat__address', 'text']
    readonly_fields = ['created_at']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'pure_phone', 'display_flats']
    raw_id_fields = ['owned_flats']  
    search_fields = ['full_name', 'phone_number', 'pure_phone']

    def display_flats(self, obj):
        flats = obj.owned_flats.all()[:3]  
        flats_list = ", ".join(flat.address for flat in flats)
        if obj.owned_flats.count() > 3:
            flats_list += ", ..."
        return flats_list
    display_flats.short_description = 'Квартиры'

    