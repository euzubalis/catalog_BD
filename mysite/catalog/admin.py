from django.contrib import admin
from . models import Country, Manufacturer, AirConditioner, TechnicalSpecification

class AirConditionerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'country', 'power', 'price']
    list_filter = ['manufacturer', 'model_name', 'country', 'price']
    search_fields = ['model_name', 'manufacturer__name', 'country__name', 'power']

class TechnicalSpecificationAdmin(admin.ModelAdmin):
    list_display = ['get_manufacturer', 'air_conditioner', 'indoor_unit_dimensions', 'outdoor_unit_dimensions', 'energy_efficiency_class', 'operating_temperature']
    list_filter = ['air_conditioner__manufacturer', 'air_conditioner', 'energy_efficiency_class']
    search_fields = ['air_conditioner__model_name', 'air_conditioner__manufacturer__name', 'energy_efficiency_class']

    def get_manufacturer(self, obj):
        return obj.air_conditioner.manufacturer.name

    get_manufacturer.short_description = 'Gamintojas'

# Register your models here.
admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(AirConditioner, AirConditionerAdmin)
admin.site.register(TechnicalSpecification, TechnicalSpecificationAdmin)








