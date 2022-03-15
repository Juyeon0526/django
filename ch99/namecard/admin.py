from django.contrib import admin
from namecard.models import Namecard_TBL

@admin.register(Namecard_TBL)
class NamecardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tel',)
