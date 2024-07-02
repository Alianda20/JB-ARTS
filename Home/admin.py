from django.contrib import admin
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages,Message,Order

# Register your models here.

admin.site.register(Canvas)
admin.site.register(Bottles)
admin.site.register(Gallery)
admin.site.register(Testimonials)
admin.site.register(Artists)
admin.site.register(OtherImages)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','created_at')
    search_fields = ('name','email','subject','message')
    list_filter = ('created_at',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'product', 'price', 'message', 'ordered_at')
    search_fields = ('name', 'email', 'phone', 'product')
    list_filter = ('ordered_at', 'price')
admin.site.register(Message, MessageAdmin)
admin.site.register(Order, OrderAdmin)