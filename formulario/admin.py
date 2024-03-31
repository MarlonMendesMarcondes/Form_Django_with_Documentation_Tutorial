from django.contrib import admin
from .models import Formulario
# Register your models here.


class FormularioAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('nome', 'idade'),
        }),
    )
    list_display = ["nome", "idade", "data_criacao"]
    list_filter = ["data_criacao"]
admin.site.register(Formulario, FormularioAdmin)