from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Vistas existentes
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def pg_art_aseo(request):
    return render(request, 'pg_art_aseo.html')

def pg_gatos(request):
    return render(request, 'pg_gatos.html')

def pg_perros(request):
    return render(request, 'pg_perros.html')

def carrito_compras(request):
    return render(request, 'carrito_compras.html')

def producto1(request):
    return render(request, 'producto1.html')

def producto2(request):
    return render(request, 'producto2.html')

def producto3(request):
    return render(request, 'producto3.html')

def producto4(request):
    return render(request, 'producto4.html')

# Vistas CRUD para Productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    return render(request, 'detalle_producto.html', {'producto': producto})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', sku=sku)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

#Eliminacion de un producto
def eliminar_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})
