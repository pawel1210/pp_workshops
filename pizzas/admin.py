from django.contrib import admin
from .models import Pizza, Comment, Flour, Style

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Comment)
admin.site.register(Flour)
admin.site.register(Style)