from django.contrib import admin
from .models import Facility


@admin.register(Facility)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ('Fac_IDNumber', 'name', 'Comm_FacName', 'region')

