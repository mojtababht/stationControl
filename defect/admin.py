from django.contrib import admin
from .models import Station,Fault,Report


admin.site.register(Station)
admin.site.register(Fault)
admin.site.register(Report)