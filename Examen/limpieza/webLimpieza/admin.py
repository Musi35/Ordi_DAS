from django.contrib import admin
from .models import Cuadrilla, Empleado, Colonia, Actividad
from django.utils.html import format_html


class CuadrillaAdmin(admin.ModelAdmin):
    list_display = ("nombre", )
    list_filter = ("nombre", )

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "paterno", "materno", "cuadri", "puesto", "telefono")
    search_fields = ("nombre", "paterno", "materno", "cuadri", "puesto")
    list_filter = ('cuadri', "puesto")   

class ColoniaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cod_postal")
    search_fields = ("nombre", "cod_postal")

class ActividadAdmin(admin.ModelAdmin):
    list_display = ("cuadri", "id_colonia", "detalle", "imagen")
    search_fields = ("cuadri", "id_colonia")
    list_filter = ('cuadri', 'id_colonia',"detalle")
    
    def imagen(self, obj):
        return format_html('<img src="{}" width="50" height="40" />', obj.foto.url)


# Register your models in the admin site
admin.site.register(Cuadrilla, CuadrillaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Colonia, ColoniaAdmin)
admin.site.register(Actividad, ActividadAdmin)
