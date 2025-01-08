from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django import views
from .views import generar_acta_entrega
from . import views
# from .views import custom_login_view

urlpatterns = [
    
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    
    
    # Implementacion de logeo
    path('register',views.register, name="register"),
    path('clouses',views.clouses, name="clouses"),
    path('login', views.custom_login_view, name='login'),
    
    
    # Enlaces CRUD de activos
    path('list_actives', views.list_actives, name="list_actives"),
    path('add_actives', views.add_actives, name="add_actives"),
    path('update_actives/<int:idactive>', views.update_actives, name="update_actives"),
    path('delete_actives/<int:idactive>', views.delete_actives, name="delete_actives"),
   
    
    # Enlaces CRUD de usuarios
    path('list_user', views.list_user ,name='list_user'),
    path('add_user', views.add_user, name="add_user"),
    path('update_user/<int:iduser>', views.update_user, name="update_user"),
    path('delete_user/<int:iduser>', views.delete_user, name="delete_user"),
    path('data_user/update_user/<int:iduser>', views.update_user, name="update_user"),
    
    # Generar acta de entrega
    path('data_user/generar_acta_entrega/<int:iduser>/<int:user_id>/', generar_acta_entrega,name="acta_entrega"),
    path('generar_acta_entrega/<int:iduser>/<int:user_id>/', generar_acta_entrega,name="acta_entrega"),
    path('ver_actas/<int:user_id>/',views.ver_actas_entrega,name="ver_actas_entrega"),
    path('delete_ActaEntrega/<int:idacta>/', views.delete_ActaEntrega, name='delete_ActaEntrega'),

    # Importacion de usuarios y activos
    path('usuarios', views.import_usuarios, name="usuarios"),
    path('activos', views.import_activos, name="activos"), 

    # Informacion de actas del usuario
    # path('info_acta/envio_email',views.envio_email, name="email"),
    
    # Informacion general de usuarios y activos
    path('data_user/<int:iduser>',views.data_user, name="data_user"),
    path('data_activo/<int:idactivo>',views.data_activo,name="data_activo"),
    path('detail_active/<int:iduser>/<int:user_id>/', views.detail_active, name="detail_active"),
    path('devolver_activo/<int:asignacion_id>/', views.devolver_activo, name='devolver_activo'),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

