from django.contrib import admin
from cap_location.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "lat", "lng"]

admin.site.register(Location, LocationAdmin)
