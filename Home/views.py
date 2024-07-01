from django.shortcuts import render,redirect
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages,Message
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
        )

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
