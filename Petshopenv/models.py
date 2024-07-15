from django.db import models

class Categoria(models.Model):
    sku = models.AutoField(primary_key=True)  # Auto-generado para cada categoría
    nombre = models.CharField(max_length=50)
    img = models.ImageField(upload_to="imagenes_categoria", null=True, blank=True)

    def __str__(self):
        return f"[{self.sku}] {self.nombre}"

class Producto(models.Model):
    sku = models.AutoField(primary_key=True)  # Cambiado de IntegerField a AutoField para auto-generación
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)  # Se asegura que el precio tenga un valor por defecto de 0
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="imagenes_producto")

    def __str__(self):
        return f"[{self.sku}] {self.nombre} - {self.descripcion}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    gmail = models.EmailField(unique=True)  # Cambiado de CharField a EmailField para mejorar la validación de emails
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"[{self.username}] {self.nombre}"
