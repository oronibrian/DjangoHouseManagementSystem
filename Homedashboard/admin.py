from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(House)
admin.site.register(Tenant)
admin.site.register(HouseCategory)
admin.site.register(Price)