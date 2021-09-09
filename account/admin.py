from django.contrib import admin
from django.utils import timezone

from .models import Contract
from django.utils.formats import date_format

# Register your models here.
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_user_from', 'get_user_to', 'create_time'
    )

    def get_user_from(self,obj):
        return obj.user_from
    get_user_from.short_description = '追蹤者'

    def get_user_to(self,obj):
        return obj.user_to
    get_user_to.short_description = '被追蹤者'

    def create_time(self,obj):
        # class_date = timezone.localtime(obj.created)
        return date_format(obj.created,'Y-m-d H:m:s')

