from django.db import models
from django.utils import timezone


class work(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)

class Meta:

    verbose_name_plural = "woks"

def __str__(self):
    return self.name

    

class store(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100,null=False, default=None)
    marc_model = models.CharField(max_length=100,null=False,default=None)
    serie = models.CharField(max_length=100,null=False,default=None)
    estade = models.CharField(max_length=50, null=False, default=None)
    observations = models.CharField(max_length=200, null=False,default=None)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'store'

    def __str__(self):
        return self.name


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,null=False)
    lastname = models.CharField(max_length=30, null=False)
    gmail = models.CharField(max_length=50, default=None)
    area = models.CharField(max_length=60,null=False)
    post = models.CharField(max_length=60,null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(store, on_delete=models.CASCADE, null= True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class ActaEntrega(models.Model):
    id = models.AutoField(primary_key=True)
    Users = models.ForeignKey(Users, on_delete=models.CASCADE)  # Establece la relación con la tabla de usuarios
    archivo_pdf = models.FileField(upload_to='actas_entrega_pdfs/')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'Acta de entrega para {self.usuario.name} {self.usuario.lastname}'



class delivery_record(models.Model):
    id = models.AutoField(primary_key=True)
    delivery_date = models.DateTimeField(auto_now_add=True)

    work = models.ForeignKey(work, on_delete=models.CASCADE)

    class  Meta:
        verbose_name_plural='delivery_record'

    def __str__(self):
        return self.name



# tabla agregaba para controlar el contador de actas


class Contador(models.Model):
    valor = models.IntegerField(default=0)




