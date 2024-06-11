from django.contrib import admin
from .models import Mascota, Adoptante, Adopcion

admin.site.register(Mascota)
admin.site.register(Adoptante)
admin.site.register(Adopcion)
