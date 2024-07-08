from django.shortcuts import render
from django.http import HttpResponse
from .models import Manufacturer, Country, AirConditioner, TechnicalSpecification
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import DetailView


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

class AirConditionerListView(generic.ListView):
    model = AirConditioner
    context_object_name = 'airconditioners'
    template_name = 'airconditioners.html'
    paginate_by = 5

class AirConditionerDetailView(generic.DetailView):
    model = AirConditioner
    context_object_name = 'airconditioner'
    template_name = 'airconditioner.html'

class TechnicalSpecificationListView(ListView):
    model = TechnicalSpecification
    template_name = 'technicalspecifications.html'
    context_object_name = 'technicalspecifications'
    paginate_by = 10

class TechnicalSpecificationDetailView(DetailView):
    model = TechnicalSpecification
    template_name = 'technicalspecification.html'
    context_object_name = 'technicalspecification'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        print(obj.__dict__)  # išvesti objekto duomenis
        return obj






