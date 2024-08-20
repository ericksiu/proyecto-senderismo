# modelos/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Comentario, Viaje, Reserva, Tours
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'apellidos', 'is_staff', 'is_superuser')
    search_fields = ('email', 'nombre', 'apellidos')

admin.site.register(Usuario, UsuarioAdmin)
class AdministrarComentario(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentario)

class AdministrarViaje(admin.ModelAdmin):
    list_display = ['id', 'destino']
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Viaje, AdministrarViaje)

class AdministrarReserva(admin.ModelAdmin):
    list_display = ('id', 'usuario')  # Adjust as needed
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Reserva, AdministrarReserva)

class AdministrarTours(admin.ModelAdmin):
    list_display = ('destino', 'precio')  # Adjust as needed
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id', 'updated')

admin.site.register(Tours, AdministrarTours)