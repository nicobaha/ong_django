from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100, blank=True, null=True)  # Opcional
    fecha_nacimiento_aproximada = models.DateField(blank=True, null=True)  # Opcional
    genero = models.CharField(max_length=10, choices=[('M', 'Macho'), ('F', 'Hembra')])
    fecha_ingreso = models.DateField()
    fecha_adopcion = models.DateField(blank=True, null=True)  # Opcional
    estado = models.CharField(max_length=20, default='Disponible', choices=[
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
        # ... otros estados posibles
    ])
    # Otros campos... (color, tamaño, descripción, etc.)

    def __str__(self):
        return self.nombre


class Adoptante(models.Model):
    rut = models.CharField(max_length=12, blank=True, null=True)  # Opcional
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255, blank=True, null=True)  # Opcional
    apellido_materno = models.CharField(max_length=255, blank=True, null=True)  # Opcional
    fecha_nacimiento = models.DateField(blank=True, null=True)  # Opcional
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')], blank=True, null=True)  # Opcional
    telefono = models.CharField(max_length=20, blank=True, null=True)  # Opcional
    email = models.EmailField(blank=True, null=True)  # Opcional
    direccion = models.TextField(blank=True, null=True)  # Opcional
    fecha_ingreso = models.DateField()
    # Otros campos... (estado civil, número de hijos, etc.)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"


class Adopcion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    fecha_adopcion = models.DateField()
    # Otros campos... (notas, documentos, etc.)

    def __str__(self):
        return f"Adopción de {self.mascota} por {self.adoptante}"
