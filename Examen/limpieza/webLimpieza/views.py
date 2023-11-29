from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Cuadrilla, Empleado, Actividad

def pagina_login(request):
    if request.method == 'POST':
        username = request.POST.get('nombre')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenido has iniciado sesion')
            return redirect('index')

        else:
            messages.warning(request, '¡Contraseña o usuario incorrecto!')

    return render(request, 'user/login.html', {
        'title': 'Login'
    })

def pagina_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login') 
def get_data(request):
    cuadrillas = Cuadrilla.objects.all()
    data = []

    for cuadrilla in cuadrillas:
        actividades_count = Actividad.objects.filter(cuadri=cuadrilla).count()

        data.append({
            'cuadrilla': cuadrilla.nombre,
            'actividades_count': actividades_count,
        })

    return JsonResponse(data, safe=False)

@login_required(login_url='login')
def dashboard(request):
    # Obtener los datos llamando a la vista get_data
    data_response = get_data(request)

    # Acceder a la propiedad content y decodificarla como una cadena
    data = data_response.content.decode('utf-8')

    # Pasar los datos a la plantilla 'webLimpieza/dashboard.html'
    return render(request, 'webLimpieza/dashboard.html', {
        'title': 'Dashboard',
        'data': data
    })

@login_required(login_url='login')
def tabla(request):
    cuadrillas = Cuadrilla.objects.all()
    data = []

    for cuadrilla in cuadrillas:
        jefe_cuadrilla = Empleado.objects.filter(cuadri=cuadrilla, puesto='jefe_cuadrilla').first()
        empleados_count = Empleado.objects.filter(cuadri=cuadrilla).count()

        data.append({
            'cuadrilla': cuadrilla.nombre,
            'jefe_cuadrilla': f'{jefe_cuadrilla.nombre} {jefe_cuadrilla.paterno} {jefe_cuadrilla.materno}' if jefe_cuadrilla else '',
            'empleados_count': empleados_count,
        })

    return render(request, 'webLimpieza/tabla.html', {
        'title': 'Informacion de las cuadrillas',
        'cuadrillas': cuadrillas, 
        'data': data
    })