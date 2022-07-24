from django.contrib import admin

from AppCoder.views import familiar
from .models import *


# Register your models here.

admin.site.register(Familiar)
admin.site.register(Animales)
admin.site.register(Vehiculos)
admin.site.register(Avatar)
admin.site.register(Post)