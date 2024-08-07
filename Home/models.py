from django.db import models


# Create your models here.


# Canvas & Bottle Paintings Class


class OtherImages(models.Model):
    image = models.ImageField(upload_to='otherImages')


class Canvas(models.Model):
    image = models.ImageField(upload_to='prodpics')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    medium = models.CharField(max_length=100)


class Bottles(models.Model):
    image = models.ImageField(upload_to='prodpics')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    medium = models.CharField(max_length=100)


class Gallery(models.Model):
    image = models.ImageField(upload_to='prodpics')


class Testimonials(models.Model):
    image = models.ImageField(upload_to='testimonialpics')
    testimonial = models.TextField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Artists(models.Model):
    image = models.ImageField(upload_to='artistpics')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)
    ordered_at = models.DateTimeField(auto_now_add=True)