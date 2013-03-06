from cap_location.models import Location


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
