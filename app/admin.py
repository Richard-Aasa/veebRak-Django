from django.contrib import admin

from .models import Birth
from .models import omanikud
from .models import raamatud

admin.site.register(Birth)
admin.site.register(omanikud)
admin.site.register(raamatud)
