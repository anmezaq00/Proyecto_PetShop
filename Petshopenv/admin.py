from django.contrib import admin
from .models import Producto, Categoria, Usuario

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'img')
    search_fields = ('nombre', 'sku')  
    list_filter = ('categoria',)
    raw_id_fields = ('categoria',)  

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'img')
    search_fields = ('nombre',)  

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'gmail')
    search_fields = ('username', 'nombre')  


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
