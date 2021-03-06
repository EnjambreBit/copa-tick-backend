from django.contrib import admin
from copatic.models.insignia import Insignia

class InsigniaAdmin(admin.ModelAdmin):
    model = Insignia
    list_display = ('id', 'nombre', 'slug')
    search_fields = ['nombre']
