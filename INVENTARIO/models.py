from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator



class work(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, default='Nombre por defecto')
    correo = models.EmailField(max_length=100, null=False, unique=True, default='correo@ejemplo.com')
    contraseña = models.CharField(max_length=100, null=False, default='contraseña123')
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)

class Meta:

    verbose_name_plural = "works"

def __str__(self):
    return f"{self.correo}" 


# activo
class activo(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    sede = models.CharField(max_length=50, default='')
    pabellon = models.CharField(max_length=5, default='')
    tipo_ambiente = models.CharField(max_length=20, default='')
    ambiente = models.CharField(max_length=100,  default='')
    direccion = models.CharField(max_length=50, default='')
    distrito = models.CharField(max_length=50, default='')
    serie = models.CharField(max_length=50, default='')
    codigo_inventario = models.CharField(max_length=50, default='')
    categoria = models.CharField(max_length=50, default='')
    marca = models.CharField(max_length=50, default='')
    descripcion = models.TextField()  # Cambiado a TextField
    modelo = models.CharField(max_length=50, default='')
    hostname = models.CharField(max_length=50, default='hs')
    estado = models.CharField(max_length=50, default='')
    renta = models.CharField(max_length=5, default='')
    contrato = models.CharField(max_length=50, default='')
    estado_renta = models.CharField(max_length=50, default='')
    proveedor = models.CharField(max_length=50, default='')
    devolucion = models.CharField(max_length=50, default='')
    declaracion = models.CharField(max_length=20, default= 'ACTIVO')

    class Meta:
        db_table = 'activo'

    def __str__(self):
        return f"{self.serie}"


class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    
    planilla = models.CharField(max_length=10, default='')
    unidad_de_negocio = models.CharField(max_length=50, default='')
    area_de_trabajo = models.CharField(max_length=100, default='')
    sub_area_de_trabajo = models.CharField(max_length=100, default='')
    ubicacion_fisica = models.CharField(max_length=20, default='')
    local = models.CharField(max_length=20, default='')
    naturaleza_de_puesto = models.CharField(max_length=100, default='')
    nomenclatura_de_puesto = models.CharField(max_length=100, default='')
    tipo_de_puesto = models.CharField(max_length=20, default='')
    motivo_de_alta = models.CharField(max_length=100, default='')
    codigo_de_personal = models.BigIntegerField(default=0)
    apellidos_y_nombres_adryan = models.CharField(max_length=100, default='')
    genero_adryan = models.CharField(max_length=20, default='')
    fecha_de_ingreso = models.DateField(default='1900-01-01')
    tipo_de_contrato_adryan = models.CharField(max_length=50, default='')
    tipo_de_jornada_adryan = models.CharField(max_length=50, default='')
    nacionalidad_adryan = models.CharField(max_length=20, default='')
    tiempo_de_servicio_anios = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    tiempo_de_servicio_meses = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(12)])
    tiempo_de_servicio_dias = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(31)])
    correo_corporativo_adryan = models.CharField(max_length=100, default='')
    fecha_de_nacimiento_adryan = models.DateField(default='1900-01-01')
    edad_adryan = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    generacion_adryan = models.CharField(max_length=50, default='')
    jefe_inmediato_jerarquico = models.CharField(max_length=100, default='')
    reemplaza_a = models.CharField(max_length=100, default='')
    activo = models.ManyToManyField(activo, related_name='usuarios')
    


    class Meta:
        db_table = 'UserData'

    def __str__(self):
        return self.apellidos_y_nombres_adryan

class AsignacionActivo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(UserData, on_delete=models.CASCADE)
    activo = models.ForeignKey(activo, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null= True, blank= True)


    class Meta:
        verbose_name = 'Asignación de Activo'
        verbose_name_plural = 'Asignaciones de Activos'
        db_table = 'AsignacionActivo'

    def __str__(self):
        return f'{self.usuario.apellidos_y_nombres_adryan} - {self.activo.serie} - {self.fecha_asignacion}'

    @property
    def duracion_dias(self):
        if self.fecha_devolucion:
            return (self.fecha_devolucion - self.fecha_asignacion).days
        return None
    

class actaEntrega(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(UserData, on_delete=models.CASCADE)  # Establece la relación con la tabla de usuarios
    archivo_pdf = models.FileField(upload_to='actas_entrega_pdfs/')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'Acta de entrega para {self.usuario.apellidos_y_nombres_adryan}'



class delivery_record(models.Model):
    id = models.AutoField(primary_key=True)
    delivery_date = models.DateTimeField(auto_now_add=True)

    work = models.ForeignKey(work, on_delete=models.CASCADE)

    class  Meta:
        verbose_name_plural='delivery_record'

    def __str__(self):
        return self.apellidos_y_nombres_adryan



# tabla agregaba para controlar el contador de actas


class Contador(models.Model):
    valor = models.IntegerField(default=0)



