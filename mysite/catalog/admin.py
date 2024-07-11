from django.contrib import admin
from . models import Country, Manufacturer, AirConditioner, TechnicalSpecification, ConditionerOrder

class AirConditionerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'country']
    list_filter = ['manufacturer', 'model_name', 'country']
    search_fields = ['model_name', 'manufacturer__name', 'country__name']

class TechnicalSpecificationAdmin(admin.ModelAdmin):
    list_display = ['get_manufacturer', 'air_conditioner', 'indoor_unit_dimensions', 'outdoor_unit_dimensions', 'energy_efficiency_class', 'operating_temperature', 'power', 'price']
    list_filter = ['air_conditioner__manufacturer', 'air_conditioner', 'energy_efficiency_class', 'power', 'price']
    search_fields = ['air_conditioner__model_name', 'air_conditioner__manufacturer__name', 'energy_efficiency_class', 'power', 'price']

    def get_manufacturer(self, obj):
        return obj.air_conditioner.manufacturer.name

    get_manufacturer.short_description = 'Gamintojas'

class ConditionerOrderAdmin(admin.ModelAdmin):
    list_display = ['air_conditioner', 'client', 'date_created']

# Register your models here.
admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(AirConditioner, AirConditionerAdmin)
admin.site.register(TechnicalSpecification, TechnicalSpecificationAdmin)
admin.site.register(ConditionerOrder, ConditionerOrderAdmin)