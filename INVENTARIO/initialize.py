# en initialize.py

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import work

def initialize_groups_and_permissions():
    # Obtener el contenido del modelo Work (tu modelo de usuario personalizado)
    content_type = ContentType.objects.get_for_model(work)

    # Crear los grupos
    grupo_usuario, creado = Group.objects.get_or_create(name='Usuario')
    grupo_administrador, creado = Group.objects.get_or_create(name='Administrador')

    # Obtener los permisos que deseas asignar
    permiso_agregar_activo = Permission.objects.get(content_type=content_type, codename='add_actives')
    permiso_agregar_usuario = Permission.objects.get(content_type=content_type, codename='add_user')

    # Asignar los permisos a los grupos
    grupo_usuario.permissions.add(permiso_agregar_activo)
    grupo_administrador.permissions.add(permiso_agregar_activo)
    grupo_administrador.permissions.add(permiso_agregar_usuario)

# Llamar a la función para inicializar los grupos y permisos
initialize_groups_and_permissions()
