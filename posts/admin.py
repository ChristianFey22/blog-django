from django.contrib import admin
from .models import Post

admin.site.site_header = "Administracion de Mi Blog Inmobiliario"
admin.site.site_title = "Panel del Blog"
admin.site.index_title = "Gestión de contenidos"
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_creacion", "estado")
    search_fields = ("titulo", "contenido", "autor")
    list_filter = ("estado", "fecha_creacion")
    list_editable = ("estado",)