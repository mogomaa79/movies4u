from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Film)
admin.site.register(User)
admin.site.register(Star)
admin.site.register(Director)
admin.site.register(Genre)