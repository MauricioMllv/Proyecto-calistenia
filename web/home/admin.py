from django.contrib import admin
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

admin.site.register(Slider, SliderAdmin)