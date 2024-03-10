from django.contrib import admin
from .models import Device
# Register your models here.


from django.contrib import admin
from .models import Device



from django.contrib import admin
from .models import Device

# Custom admin action to delete all inactive devices
def delete_inactive_devices(modeladmin, request, queryset):
    queryset.filter(status='INACTIVE').delete()
delete_inactive_devices.short_description = "Delete all inactive devices"

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'name', 'status')
    actions = [delete_inactive_devices]










