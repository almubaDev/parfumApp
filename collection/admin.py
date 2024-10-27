from django.contrib import admin
from .models import Note, Brand, Fragrance, Item, Collection
from .forms import FragranceAdminForm



class NoteAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(Note, NoteAdmin)

class BrandAdmin(admin.ModelAdmin):
    ordering = ['name']
    
admin.site.register(Brand)


class FragranceAdmin(admin.ModelAdmin):
    filter_horizontal = ('top_notes', 'middle_notes', 'base_notes')
    form = FragranceAdminForm
    ordering = ['name']
    
admin.site.register(Fragrance, FragranceAdmin)


class ItemAdmin(admin.ModelAdmin):
    ordering = ['parfum']
    
admin.site.register(Item, ItemAdmin)


class CollectionAdmin(admin.ModelAdmin):
    ordering = ['user']
    
admin.site.register(Collection, CollectionAdmin)