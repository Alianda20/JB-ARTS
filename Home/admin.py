from django.contrib import admin
from .models import Canvas, Bottles, Gallery, Testimonials, Artists, OtherImages,Message

# Register your models here.

admin.site.register(Canvas)
admin.site.register(Bottles)
admin.site.register(Gallery)
admin.site.register(Testimonials)
admin.site.register(Artists)
admin.site.register(OtherImages)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','created_at')
    search_fields = ('name','email','subject','message')