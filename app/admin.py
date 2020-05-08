from django.contrib import admin

# Register your models here.
from app.models import Moment,Mytable
admin.site.register(Moment)
admin.site.register(Mytable)