from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        ) #send email
        email_message = f"Message:\n{message}\n\n\n Regards From:\n{name}\n{email}"
        try:
            send_mail(
                subject,  # Subject of the email
                email_message,  # Message content
                email,  # From email
                ['kelalianda@gmail.com','josephbarasa622@gmail.com','1046089@cuea.edu']  # To email list
            )
            messages.success(request, 'You have received an email')
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, 'Failed to send email.')

        # Return 'OK' to satisfy the JavaScript condition for success
        return HttpResponse('OK', content_type='text/plain')


    canvas = Canvas.objects.all()
    bottle = Bottles.objects.all()
    gall = Gallery.objects.all()
    testimonial = Testimonials.objects.all()
    artist = Artists.objects.all()
    otherImages = OtherImages.objects.all()
    return render(request, 'index.html',
                  {'canvas': canvas, 'bottle': bottle, 'gall': gall,
                   'testimonial': testimonial, 'artist': artist,
                   'otherImages': otherImages}
                  )

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        product = request.POST.get('product')
        price = request.POST.get('price')
        address = request.POST.get('address')

        Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            product=product,
            price=price,
            address=address
        )  # send email

        subject = f"A NEW ORDER PLACED FOR {product}"
        email_message = f"An order has been placed for {product} KSH {price}\n\nOrder placed by:\n{name}  {phone}\n{email}\n{address}"
        try:
            send_mail(
                subject,  # Subject of the email
                email_message,  # Message content
                email,  # From email
                ['kelalianda@gmail.com', 'josephbarasa622@gmail.com', '1046089@cuea.edu']  # To email list
            )
            messages.success(request, 'You have received an email')
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, 'Failed to send email.')

    return render(request,'checkout.html')
