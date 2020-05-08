from django.contrib import admin

# Register your models here.
from .models import PYnews, Comments
admin.site.register(PYnews)
admin.site.register(Comments)
