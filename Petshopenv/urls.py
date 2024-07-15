from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz que lleva a la página principal
    path('login/', views.login, name='login'),  # Ruta para la página de login
    path('registro/', views.registro, name='registro'),  # Ruta para la página de registro
    path('pg_art_aseo/', views.pg_art_aseo, name='pg_art_aseo'),  # Ruta para la página de artículos de aseo
    path('pg_gatos/', views.pg_gatos, name='pg_gatos'),  # Ruta para la página de gatos
    path('pg_perros/', views.pg_perros, name='pg_perros'),  # Ruta para la página de perros
    path('carrito_compras/', views.carrito_compras, name='carrito_compras'),  # Ruta para la página del carrito de compras
    path('producto1/', views.producto1, name='producto1'),  # Ruta para la página del producto1
    path('producto2/', views.producto2, name='producto2'),  # Ruta para la página del producto2
    path('producto3/', views.producto3, name='producto3'),  # Ruta para la página del producto3
    path('producto4/', views.producto4, name='producto4'),  # Ruta para la página del producto4
    # Rutas CRUD para Productos
    path('productos/', views.lista_productos, name='lista_productos'),  # Ruta para listar todos los productos
    path('productos/detalle/<int:sku>/', views.detalle_producto, name='detalle_producto'),  # Ruta para el detalle de un producto
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),  # Ruta para agregar un nuevo producto
    path('productos/editar/<int:sku>/', views.editar_producto, name='editar_producto'),  # Ruta para editar un producto existente
    path('productos/eliminar/<int:sku>/', views.eliminar_producto, name='eliminar_producto'),  # Ruta para eliminar un producto
]
