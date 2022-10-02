from django.contrib import admin
from .models import Fromage


class FromageAdmin(admin.ModelAdmin):
    list_display = ("name", "origin", "category", "description", "composition", "stock", "thumbnail", "price",)
    search_fields = ['name']


admin.site.register(Fromage, FromageAdmin)
