from django.shortcuts import render
from django.http import HttpResponse
from .models import Manufacturer, Country
# Create your views here.
def index(request):
    num_manufacturer = Manufacturer.objects.all().count()
    num_country = Country.objects.all().count()
    context = {
        'num_manufacturer': num_manufacturer,
        'num_country': num_country,
    }
    return render(request, template_name="index.html", context=context)

def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    context = {
        "manufacturers": manufacturers,
    }
    return render(request, template_name="manufacturers.html", context=context)

def manufacturer(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
    context = {
        "manufacturer": manufacturer,
    }
    return render(request, template_name="manufacturer.html", context=context)




