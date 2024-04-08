from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404
from .models import activo, Users, ActaEntrega,Contador
from django.db.models import Q
from .models import Contador
from .forms import ActaEntregaForm
from django.core.mail import EmailMessage
from io import BytesIO
from datetime import datetime

from docx.shared import RGBColor
from docx.oxml.ns import nsdecls
from docx.opc.constants import RELATIONSHIP_TYPE as RT

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docxtpl import DocxTemplate

import pandas as pd
import xml.etree.ElementTree as ET
import locale

from docx.oxml import parse_xml

from django.contrib.auth import login as django_login

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm  
from django.contrib.auth.models import  User
from django.contrib.auth import login,logout,authenticate
from django.db import  IntegrityError

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

#CREATE-DELETE-LIST AND UPDATE MODEL ACTIVE--->
#===============#===========================#

def index (request):
    return render(request, "index.html")


def register (request):
    
    if request.method == 'GET':
        return render (request, 'acces_user/register.html',{
            'form':UserCreationForm
        })
    
    else:
        if request.POST['password1']== request.POST['password2']:
            #register user
           try: 
                user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request,user)
                return  redirect('index') 
           except IntegrityError:  
                return render (request, 'acces_user/register.html',{
                    'form': UserCreationForm,
                    "error":'Username already exists'
                })


        return render(request, 'acces_user/register.html',{
            'form':UserCreationForm,
            "error":'Password do not match'
        })             
        
def clouses(request):
     
     logout(request)
     return redirect('Documents/data_user.html')
     
    
    
    
def login(request):
    if request.method == 'GET':
        return render(request, 'acces_user/login.html',
                      {
                          'form':AuthenticationForm
                      })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST
                     ['password'])
        
        if user is None:
            return render(request, 'acces_user/login.html',{
                'form': AuthenticationForm,
                'error': 'username or password is incorrect'
            })
        else:
             django_login(request, user)  
             return redirect('index')



def data_user(request,iduser):

    user = get_object_or_404(Users, pk=iduser)
    
    context={
        'user':user
    }
        
    
    return render(request,"Documents/data_user.html",context)
    
def data_activo(request, idactivo):
    
    activos = get_object_or_404(activo, pk=idactivo)
    
    context = {
        'activo':activos
    }
    
    return render(request, "Documents/data_activo.html",context)



def acta_entrega (request):
    return render(request, "acta_entrega.html")

def list_actives (request):
    if request.method=='POST':
        word = request.POST.get('keyword')
        list = activo.objects.all()

        if word is not None:
            resultado_busqueda = list.filter(
                 
                Q(id__icontains=word) |
                Q(serie__icontains=word)|
                Q(codigo_inventario__icontains=word)|
                Q(hostname__icontains=word) 
                
            )

            datos = {'activos': resultado_busqueda}
            return render(request, "crud_actives/list_actives.html",datos)
        else:
            datos = {'activos' : list}
            return render(request, "crud_actives/list_actives.html",datos)

    else:
        active = activo.objects.order_by('-id')[:10] 
        datos = {'activos' : active}
        return render(request, "crud_actives/list_actives.html",datos)



def add_actives (request):
    if request.method=='POST':
        if request.POST.get ('descripcion') and request.POST.get ('marc_model') and request.POST.get('serie') and request.POST.get('estado')  and request.POST.get('Observaciones'):
            
            active = activo()
            active.description = request.POST.get('descripcion')
            active.marc_model = request.POST.get('marc_model')
            active.serie = request.POST.get('serie')
            active.estade = request.POST.get('estado')
            active.observations = request.POST.get('Observaciones')
        
            active.save()
            return redirect('list_actives')
    else:        
            return render(request, "crud_actives/add_actives.html")
    

def update_actives (request, idactive  ):
    try:
        if request.method =='POST':
            if request.POST.get('id') and request.POST.get ('descripcion') and request.POST.get ('marc_model') and request.POST.get('serie') and request.POST.get('estado')  and request.POST.get('Observaciones') :
            
                user_id_old = request.POST.get('id')
                user_old = active()
                user_old = active.objects.get(id = user_id_old )
                
                active = active()
                active.id = request.POST.get('id')
                active.description = request.POST.get('descripcion')
                active.marc_model = request.POST.get('marc_model')
                active.serie = request.POST.get('serie')
                active.estade = request.POST.get('estado')
                active.observations = request.POST.get('Observaciones')
                active.fecha_registro = user_old.fecha_registro       
                active.save()
                return redirect('list_actives')
            
        else:
            
            active = active.objects.all()
            actives_id = active.objects.get(id = idactive)
            datos = {'activos' : active, 'actives_id': actives_id}
            return render(request, "crud_actives/update_actives.html",datos)

    except active.DoesNotExist:
        active = active.objects.all()
        actives_id = None
        datos = {'activos' : active, 'actives_id': actives_id}         
        return render(request, "crud_actives/update_actives.html",datos)


def delete_actives  (request, idactive):
    try:
        if request.method == 'POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla=active.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('list_actives')
        else:
            active = active.objects.all()
            actives_id = active.objects.get(id = idactive)
            datos = {'activos' : active, 'actives_id': actives_id}
            return render(request, "crud_actives/delete_actives.html",datos)
        
    except active.DoesNotExist:
        active = active.objects.all()
        actives_id = None
        datos = {'activos' : active, 'actives_id': actives_id} 
        return render(request, "crud_actives/delete_actives.html",datos)
    

#**************************#*************************************************#

    #LIST - CREATE - UPDATE AND DELETE MODEL USER

#************************#***************************************************#



def list_user(request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Users.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(id__icontains=palabra) |
                Q(area_de_trabajo__icontains=palabra) |
                Q(sub_area_de_trabajo__icontains=palabra) |
                Q(codigo_de_personal__icontains=palabra) |
                Q(apellidos_y_nombres_adryan__icontains=palabra) |
                Q(tipo_de_jornada_adryan__icontains=palabra)   |
                Q(correo_corporativo_adryan__icontains=palabra) 


            )

            datos = {'usuarios': resultado_busqueda}
            return render(request, "crud_users/list_user.html", datos)
        else:
            datos = {'usuarios': lista}
            return render(request, "crud_users/list_user.html", datos)

    else:
        usuarios = Users.objects.order_by('id')[:10]
        datos = {'usuarios': usuarios}
        return render(request, "crud_users/list_user.html", datos)



def add_user (request):
    if request.method=='POST':
        if request.POST.get ('nombre') and request.POST.get ('apellidos') and request.POST.get('gmail') and request.POST.get('area')  and request.POST.get('cargo'):
            user = Users()
            user.name = request.POST.get('nombre')
            user.lastname = request.POST.get('apellidos')
            user.gmail = request.POST.get('gmail')
            user.area = request.POST.get('area')
            user.post = request.POST.get('cargo')

            user.save()
            return redirect('list_user')
    else:
        return render(request, "crud_users/add_user.html")



def update_user (request, iduser):
    try:    
        if request.method=='POST':
            if request.POST.get('id') and request.POST.get ('nombre') and request.POST.get ('apellidos') and request.POST.get('gmail') and request.POST.get('area')  and request.POST.get('cargo'):
                
                user_id_old = request.POST.get('id')
                user_old = Users()
                user_old = Users.objects.get(id = user_id_old )
                
                user = Users()
                user.id = request.POST.get('id')
                user.name = request.POST.get('nombre')
                user.lastname = request.POST.get('apellidos')
                user.gmail = request.POST.get('gmail')
                user.area = request.POST.get('area')
                user.post = request.POST.get('cargo')
                user.fecha_registro = user_old.fecha_registro 
                user.save()
                return redirect('list_user')

        else:
            users = Users.objects.all()
            user = Users.objects.get(id=iduser)
            datos = { 'usuarios': users, 'usuario':user }
            return render(request, "crud_users/update_user.html",datos)

    except Users.DoesNotExist:
            users = Users.objects.all()
            user = None
            datos = { 'usuarios': users, 'usuario':user }
            return render(request, "crud_users/update_user.html",datos) 



def delete_user (request, iduser):
    try:
        if request.method=='POST':
            if request.POST.get('id'):
                user_a_borrar = request.POST.get('id')
                tupla = Users.objects.get(id = user_a_borrar)
                tupla.delete()
                return redirect('list_user')

        else:
            users = Users.objects.all()
            user = Users.objects.get(id = iduser)
            datos = { 'usuarios': users, 'usuario':user }
            return render(request, "crud_users/delete_user.html",datos)
        
    except Users.DoesNotExist:
        users = Users.objects.all()
        user = None
        datos = { 'usuarios': users, 'usuario':user }
        return render(request, "crud_users/delete_user.html",datos)

###############REPORTES DE USUARIOS###################



def generar_acta_entrega(request, iduser):
    usuario = get_object_or_404(Users, pk=iduser)
    activos = activo.objects.all()

    contador_obj, created = Contador.objects.get_or_create(id=1)
    contador = contador_obj.valor

    

    if request.method == 'POST' and 'generar_acta' in request.POST:
        activos_seleccionados = request.POST.getlist('activo')
        activos_entregados = activo.objects.filter(pk__in=activos_seleccionados)

        # Incrementar el contador
        contador_obj.valor += 1
        contador_obj.save()
        contador = contador_obj.valor

        # Convertir campos a mayúsculas antes de guardar
        for activo_entregado in activos_entregados:
            for field in ['categoria', 'marca', 'codigo_inventario', 'serie', 'estado']:
                setattr(activo_entregado, field, getattr(activo_entregado, field).upper())
            activo_entregado.save()

        # Cargar la plantilla de Word
        template_path = './INVENTARIO/templates/Documents/docxtemplate.docx'
        doc = DocxTemplate(template_path)
    

        context = {
            'apellidos_y_nombres_adryan': usuario.apellidos_y_nombres_adryan.upper(),
            'nomenclatura_de_puesto': usuario.nomenclatura_de_puesto.upper(),
            'area_de_trabajo': usuario.area_de_trabajo.upper(),
            'contador':contador
    
        }

        # Renderizar la plantilla con los datos
        doc.render(context)
        doc.add_paragraph("A continuación, se detallan los recursos informáticos")

        # Añadir una tabla para los activos entregados
        table = doc.add_table(rows=1, cols=6)
        table.style = 'Table Grid'
        table.autofit = True

        for cell in table.columns:
            cell.width = 5000

        # Encabezados de tabla
        headings = table.rows[0].cells
        headings[0].text = 'CANTIDAD'
        headings[1].text = 'DESCRIPCION'
        headings[2].text = 'MARCA'
        headings[3].text = 'CODIGO PATRIMONIO'
        headings[4].text = 'SERIE'
        headings[5].text = 'OBSERVACIONES'

        # Cambiar el color del fondo del encabezado a negro
        for cell in headings:
            cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)  # Color blanco
            cell._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="000000"/>'.format(nsdecls('w'))))  # Color de fondo en negro
        # parse_xml
        for cell in headings:
            cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # Alinear al centro
            

        for activo_entregado in activos_entregados:
            row_cells = table.add_row().cells
            for i in range(6):
                row_cells[i].text = "1" if i == 0 else getattr(activo_entregado, ['categoria', 'marca', 'codigo_inventario', 'serie', 'estado'][i-1])
                for paragraph in row_cells[i].paragraphs:
                    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER


        doc.add_paragraph("")
        doc.add_paragraph("El presente documento deja constancia de que los recursos fueron entregados y recepcionados sin observaciones.")
        doc.add_paragraph("IMPORTANTE:")
        doc.add_paragraph("Por favor revisen la politica de activos fijos, pues este equipo se encuentra bajo su responsabilidad. https://conecta.continental.edu.pe/")



        #######FECHA ACTUAL######
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')
        # Obtener y formatear la fecha actual
        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime('Huancayo, ' + '%A, %d de %B de %Y')

        # Concatenar textoya queda 
        texto_concatenado = fecha_formateada

        # Agregar el texto concatenado al documento
        parrafo = doc.add_paragraph(texto_concatenado)
        parrafo.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        # agregar_tabla_firma(doc, usuario.name)

        # Guardar el documento en un BytesIO para luego devolverlo como HttpResponse
        document_buffer = BytesIO()
        doc.save(document_buffer)
        document_buffer.seek(0)

        # Devolver el documento como una respuesta para que el navegador lo descargue
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename=acta_entrega_{contador}.docx'
        response.write(document_buffer.read())
        
        return response
    else:
        context = {'user': usuario, 'activos': activos, 'contador': contador}
        return render(request, 'Documents/acta_entrega.html', context)



##AREA DE PRUEBAS##

##########################


#----------------------EXPORTAR E IMPORTAR ARCHIVOS--------------------#







def import_usuarios(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_usuarios')

        if excel_file and excel_file.name.endswith('.xlsx'):
            # Leer el archivo Excel
            df = pd.read_excel(excel_file)
                 
            if all(col in df.columns for col in ['Planilla', 'Unidad de negocio','Área de trabajo','Sub Área de trabajo',
                                                 'Ubicación Física','Local ','Naturaleza de puesto','Nomenclatura de puesto',
                                                 'Tipo de puesto','Motivo de alta','Código de personal','Apellidos y nombres (ADRYAN)',
                                                 'Género (ADRYAN)','Fecha de ingreso','Tipo de contrato (ADRYAN)','Tipo de jornada (ADRYAN)',
                                                 'Nacionalidad (ADRYAN)','Tiempo de servicio (años)','Tiempo de servicio (meses)',
                                                 'Tiempo de servicio (días)','Correo corporativo (ADRYAN)','Fecha de nacimiento (ADRYAN)',
                                                 'Edad (ADRYAN)','Generación (ADRYAN)','Jefe inmediato jerárquico',
                                                 'Reemplaza a']):
                # Iterar a través de las filas del DataFrame y crear nuevos usuarios
                
            #Brinda a la fecha el formato deseado
                df['Fecha de ingreso'] = pd.to_datetime(df['Fecha de ingreso'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
                df['Fecha de nacimiento (ADRYAN)'] = pd.to_datetime(df['Fecha de nacimiento (ADRYAN)'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

                for index, row in df.iterrows():
                    usuario = Users(
                        planilla=row['Planilla'],
                        unidad_de_negocio= row['Unidad de negocio'],
                        area_de_trabajo=row['Área de trabajo'],
                        sub_area_de_trabajo=row['Sub Área de trabajo'],
                        ubicacion_fisica=row['Ubicación Física'],
                        local=row['Local '],
                        naturaleza_de_puesto=row['Naturaleza de puesto'],
                        nomenclatura_de_puesto=row['Nomenclatura de puesto'],
                        tipo_de_puesto=row['Tipo de puesto'],
                        motivo_de_alta=row['Motivo de alta'],
                        codigo_de_personal=row['Código de personal'],
                        apellidos_y_nombres_adryan=row['Apellidos y nombres (ADRYAN)'],
                        genero_adryan=row['Género (ADRYAN)'],
                        fecha_de_ingreso=row['Fecha de ingreso'],
                        tipo_de_contrato_adryan=row['Tipo de contrato (ADRYAN)'],
                        tipo_de_jornada_adryan=row['Tipo de jornada (ADRYAN)'],
                        nacionalidad_adryan=row['Nacionalidad (ADRYAN)'],
                        tiempo_de_servicio_anios=row['Tiempo de servicio (años)'],
                        tiempo_de_servicio_meses=row['Tiempo de servicio (meses)'],
                        tiempo_de_servicio_dias=row['Tiempo de servicio (días)'],
                        correo_corporativo_adryan=row['Correo corporativo (ADRYAN)'],
                        fecha_de_nacimiento_adryan=row['Fecha de nacimiento (ADRYAN)'],
                        edad_adryan=row['Edad (ADRYAN)'],
                        generacion_adryan=row['Generación (ADRYAN)'],
                        jefe_inmediato_jerarquico=row['Jefe inmediato jerárquico'],
                        reemplaza_a=row['Reemplaza a']
                    )
                    usuario.save()

            return redirect('list_user')

    return render(request, 'reports/Importar/usuarios.html')


def import_activos(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_activos')

        if excel_file and excel_file.name.endswith('.xlsx'):
            # Leer el archivo Excel
            df = pd.read_excel(excel_file)

            if all(col in df.columns for col in ['SEDE','PABELLÓN','TIPO DE AMBIENTE','AMBIENTE','DIRECCIÓN','DISTRITO','SERIE','CÓDIGO DE INVENTARIO',
                                                 'CATEGORIA','MARCA','DESCRIPCIÓN','MODELO','HOSTNAME','ESTADO','RENTA','CONTRATO','ESTADO DE RENTA','PROVEEDOR',
                                                 'DEVOLUCIÓN']):
        
                for index, row in df.iterrows():
                    active = activo( 
                        sede=row['SEDE'],
                        pabellon=row['PABELLÓN'],
                        tipo_ambiente=row['TIPO DE AMBIENTE'],
                        ambiente=row['AMBIENTE'],
                        direccion=row['DIRECCIÓN'],
                        distrito=row['DISTRITO'],
                        serie=row['SERIE'],
                        codigo_inventario=row['CÓDIGO DE INVENTARIO'],
                        categoria=row['CATEGORIA'],
                        marca=row['MARCA'],
                        descripcion=row['DESCRIPCIÓN'],
                        modelo=row['MODELO'],
                        hostname=row['HOSTNAME'],
                        estado=row['ESTADO'],
                        renta=row['RENTA'],
                        contrato=row['CONTRATO'],
                        estado_renta=row['ESTADO DE RENTA'],
                        proveedor=row['PROVEEDOR'],
                        devolucion=row['DEVOLUCIÓN']


                    )
                    active.save()

            return redirect('list_actives')


    return render(request, 'reports/Importar/activos.html')  # Renderiza el formulario de importación de activos



def export(request):
   return render(request, "reports/export.html")


def info_acta(request, iduser):
    user = Users.objects.get(pk=iduser)
    actas_entrega = ActaEntrega.objects.filter(Users=user)

    if request.method == 'POST':
        form = ActaEntregaForm(request.POST, request.FILES)
        if form.is_valid():
            acta_entrega = form.save(commit=False)
            acta_entrega.Users = user
            acta_entrega.save()
            return redirect('info_acta', iduser=user.id)


    else:
        form = ActaEntregaForm()

    return render(request, 'Info/info_acta.html', {'user': user, 'actas_entrega': actas_entrega, 'form': form})

def delete_ActaEntrega(request, idacta):
    if request.method == 'POST':
        try:
            actas_entrega = ActaEntrega.objects.get(pk=idacta)
            # Elimina el documento de la base de datos y del sistema de archivos
            actas_entrega.delete()
        except ActaEntrega.DoesNotExist:
            # Maneja el caso en el que el documento no existe
            raise Http404("El acta de entrega no existe.")
    return redirect('info_acta', iduser=actas_entrega.Users.id)
    

#------------------Envio de correo Electronico---------#

def envio_email(request):
 

    if request.method == 'POST':
        email = request.POST.get('email', '')

        if email:
            subject = 'Firma Acta Entrega'
            message = 'Estimado colaborador reciba un cordial saludo de parte del area de Tecnologia de Información en el siguiente correo adjuntamos el Acta de entrega del equipo que se le entrego a su persona, que detalla lo siguiente:'
            
            from_email = 'soporteic@continental.edu.pe'
            recipient_list = [email]
            email_message = EmailMessage(subject, message, from_email, recipient_list)
        
            if request.FILES:
                for file in request.FILES.getlist('pdf_file'):
                    email_message.attach(file.name, file.read(), file.content_type)

            email_message.send()
        
        return render(request, 'email/email.html')
    return render(request, 'email/email.html')

