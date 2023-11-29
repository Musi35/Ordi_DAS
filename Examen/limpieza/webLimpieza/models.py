from django.db import models

class Cuadrilla(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    class Meta:
        verbose_name = 'Cuadrilla'
        verbose_name_plural = 'Cuadrillas'
    
    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    PUESTO_CHOICES = [
        ('jefe_cuadrilla', 'Jefe de cuadrilla'),
        ('empleado', 'Empleado'),
    ]
    
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    paterno = models.CharField(max_length=50, verbose_name="Paterno")
    materno = models.CharField(max_length=50, verbose_name="Materno")
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    puesto = models.CharField(max_length=50, verbose_name="Puesto", choices=PUESTO_CHOICES)
    cuadri = models.ForeignKey(Cuadrilla, on_delete=models.RESTRICT, verbose_name="ID_Cuadrilla")

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return self.nombre

class Colonia(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    cod_postal = models.CharField(max_length=5, verbose_name="Codigo_Postal")

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'
    
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    cuadri = models.ForeignKey(Cuadrilla, on_delete=models.RESTRICT, verbose_name="ID_Cuadrilla")
    foto = models.ImageField(upload_to='fotos/', verbose_name="Foto", default="null")
    id_colonia = models.ForeignKey(Colonia, on_delete=models.RESTRICT, verbose_name="ID_Colonia")
    detalle = models.TextField(max_length=100, verbose_name="Detalle")

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
    
    def __str__(self):
        return f'{str(self.cuadri)}'