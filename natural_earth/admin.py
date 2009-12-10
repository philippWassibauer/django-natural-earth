from django.contrib.gis import admin
from natural_earth.models import County, Country

admin.site.register(Country, admin.GeoModelAdmin)



class CountyAdmin(admin.GeoModelAdmin):
    list_display        = ('name', 'name_1', 'region', 'engtype_1', 'nev_countr')
    list_filter         = ('name', 'nev_countr')
    search_fields       = ('name', 'name_1', 'region', 'engtype_1', 'nev_countr')
    
admin.site.register(County, CountyAdmin)


