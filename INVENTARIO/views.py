from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import store, Users
from django.db.models import Q

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

#CREATE-DELETE-LIST AND UPDATE MODEL ACTIVE--->
#===============#===========================#

def index (request):
    return render(request, "index.html")

def list_actives (request):
    if request.method=='POST':
        word = request.POST.get('keyword')
        list = store.objects.all()

        if word is not None:
            resultado_busqueda = list.filter(
                 Q(id__icontains=word) |
                 Q(n_serie__icontains=word) | 
                 Q(marca__icontains=word)
            )

            datos = {'stores': resultado_busqueda}
            return render(request, "crud_actives/list_actives.html",datos)
        else:
            datos = {'stores' : list}
            return render(request, "crud_actives/list_actives.html",datos)

    else:
        active = store.objects.order_by('-id')[:10] 
        datos = {'stores' : active}
        return render(request, "crud_actives/list_actives.html",datos)



def add_actives (request):
    if request.method=='POST':
        if request.POST.get ('descripcion') and request.POST.get ('marc_model') and request.POST.get('serie') and request.POST.get('estado')  and request.POST.get('Observaciones'):
            
            active = store()
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
                user_old = store()
                user_old = store.objects.get(id = user_id_old )
                
                active = store()
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
            
            active = store.objects.all()
            actives_id = store.objects.get(id = idactive)
            datos = {'stores' : active, 'actives_id': actives_id}
            return render(request, "crud_actives/update_actives.html",datos)

    except store.DoesNotExist:
        active = store.objects.all()
        actives_id = None
        datos = {'stores' : active, 'actives_id': actives_id}         
        return render(request, "crud_actives/update_actives.html",datos)


def delete_actives  (request, idactive):
    try:
        if request.method == 'POST':
            if request.POST.get('id'):
                id_a_borrar = request.POST.get('id')
                tupla=store.objects.get(id = id_a_borrar)
                tupla.delete()
                return redirect('list_actives')
        else:
            active = store.objects.all()
            actives_id = store.objects.get(id = idactive)
            datos = {'stores' : active, 'actives_id': actives_id}
            return render(request, "crud_actives/delete_actives.html",datos)
        
    except store.DoesNotExist:
        active = store.objects.all()
        actives_id = None
        datos = {'stores' : active, 'actives_id': actives_id} 
        return render(request, "crud_actives/delete_actives.html",datos)
    

#**************************#*************************************************#

    #LIST - CREATE - UPDATE AND DELETE MODEL USER

#************************#***************************************************#


def list_user (request):
    if request.method == 'POST':
        palabra = request.POST.get('keyword')
        lista = Users.objects.all()

        if palabra is not None:
            resultado_busqueda = lista.filter(
                    Q(id__icontains=palabra) |
                    Q(name__icontains= palabra) |
                    Q(lastname__icontains = palabra) |
                    Q(area__icontains=palabra)
            )

            datos = { 'usuarios': resultado_busqueda }
            return render(request, "crud_users/list_user.html", datos)
        else:
            datos = { 'usuarios': lista }
            return render(request, "crud_users/list_user.html", datos)

    else:
        users = Users.objects.order_by('id')[:10]
        datos = { 'usuarios': users }
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
