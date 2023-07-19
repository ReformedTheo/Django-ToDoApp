from django.contrib import admin
from todoApp.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','status','user')

admin.site.register(Evento, EventoAdmin)