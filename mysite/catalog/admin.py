from django.contrib import admin
from . models import Country, Manufacturer, AirConditioner, TechnicalSpecification

class AirConditionerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model_name', 'country', 'power', 'price']
    list_filter = ['manufacturer', 'country', 'price']

class TechnicalSpecificationAdmin(admin.ModelAdmin):
    list_display = ['air_conditioner', 'indoor_unit_dimensions', 'outdoor_unit_dimensions', 'energy_efficiency_class', 'operating_temperature']
    list_filter = ['air_conditioner', 'energy_efficiency_class']

# Register your models here.
admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(AirConditioner, AirConditionerAdmin)
admin.site.register(TechnicalSpecification, TechnicalSpecificationAdmin)




