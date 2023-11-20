from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
import os
from dotenv import load_dotenv
load_dotenv()

def cotizacion(request):
    return render(request, 'cotizacion.html', {})

def enviar_cotizacion(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        nombre = request.POST.get('name')
        telefono = request.POST.get('telefono')
        destino = request.POST.get('destino')
        origen = request.POST.get('origen')
        adultos = request.POST.get('adultos')
        menores = request.POST.get('menores')
        acomodo_habitaciones = request.POST.get('acomodo_habitaciones')
        todo_incluido = request.POST.get('todo_incluido')
        hospedaje = request.POST.get('hospedaje')
        sencillo = request.POST.get('sencillo')
        desde = request.POST.get('desde')
        hasta = request.POST.get('hasta')
        comentarios = request.POST.get('comentarios')

        template = render_to_string('email_template.html', {
            'subject': subject,
            'nombre': nombre,
            'telefono': telefono,
            'destino': destino,
            'origen': origen,
            'adultos': adultos,
            'menores': menores,
            'acomodo_habitaciones': acomodo_habitaciones,
            'todo_incluido': todo_incluido,
            'hospedaje': hospedaje,
            'sencillo': sencillo,
            'desde': desde,
            'hasta': hasta,
            'comentarios': comentarios,
        })
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            [os.getenv('CORREO')] #correo que recibira el mensaje
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Correo enviado correctamente, en unos momentos nos pondremos en contacto contigo por Whatsapp.')
        return redirect('cotizacion')