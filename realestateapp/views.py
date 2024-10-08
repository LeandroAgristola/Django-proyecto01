from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from .models import Desarrollo

def home(request):
    desarrollos = Desarrollo.objects.all()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            # Extraer datos del formulario validado
            nombre = formulario_contacto.cleaned_data['nombre']
            apellido = formulario_contacto.cleaned_data['apellido']
            telefono = formulario_contacto.cleaned_data['telefono']
            email = formulario_contacto.cleaned_data['email']
            consulta = formulario_contacto.cleaned_data['consulta']

            # Configuración del email
            email_message = EmailMessage(
                "Mensaje desde App Django",
                f"Nombre: {nombre} {apellido}\nTeléfono: {telefono}\nEmail: {email}\nConsulta: {consulta}",
                "#",  # Tu dirección de correo (debe coincidir con EMAIL_HOST_USER)
                ["#"],  # Dirección a la que llega el correo
                reply_to=[email]
            )

            try:
                # email_message.send()  # Envío real del correo (DESCOMENTAR en producción)
                # Simulación de envío exitoso, comentar para la funcionalidad real
                return JsonResponse({'status': 'ok'}, status=200)
            except Exception as e:
                # Mostrar el error en la consola (DESCOMENTAR en producción)
                # print(f"Error al enviar el correo: {e}")
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        else:
            # Enviar errores de validación al frontend en formato JSON
            errores = formulario_contacto.errors.as_json()
            return JsonResponse({'status': 'invalid', 'errors': errores}, status=400)
    
    # Cargar el formulario para GET request
    formulario_contacto = FormularioContacto()
    return render(request, 'realestateapp/home.html', {
        'desarrollos': desarrollos, 
        'miformulario': formulario_contacto
    })

def mobileViviendas(request):
    return render(request, 'realestateapp/mobileViviendas.html')

def mobileEdificios(request):
    return render(request, 'realestateapp/mobileEdificios.html')

def mobileIndustrias(request):
    return render(request, 'realestateapp/mobileIndustrias.html')
