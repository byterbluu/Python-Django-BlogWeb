from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage   
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            email = EmailMessage(
                'Mensaje de contacto',
                'De {} {}\n\nEscribió:\n\n{}'.format(name, email, message),
                "lasabrosa.com", #EMAIL DE ORIGEN"
                ["josepinadevbusiness@gmail.com"], #EMAIL DE DESTINO
                reply_to=[email]
            )
            #LO ENVIAREMOS Y REDIRECCIONAREMOS
            try:
                email.send()
                # HA IDO BIEN, REDIRECCIONAMOS OK
                return redirect(reverse('contact')+"?ok")
            except:
                # HA OCURRIDO UN ERROR, REDIRECCIONAMOS ERROR
                return redirect(reverse('contact')+"?error")

    return render(request, 'contact/contact.html', {'form': contact_form})