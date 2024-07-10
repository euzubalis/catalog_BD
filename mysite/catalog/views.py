from django.shortcuts import render
from .models import Manufacturer, Country, AirConditioner, TechnicalSpecification
from django.views import generic
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import password_validation

# Create your views here.
def index(request):
    num_manufacturer = Manufacturer.objects.all().count()
    num_country = Country.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_manufacturer': num_manufacturer,
        'num_country': num_country,
        'num_visits': num_visits,
    }
    return render(request, template_name="index.html", context=context)

def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    paginator = Paginator(manufacturers, per_page=3)
    page_number = request.GET.get('page')
    paged_manufacturers = paginator.get_page(page_number)
    context = {
        "manufacturers": paged_manufacturers,
    }
    return render(request, template_name="manufacturers.html", context=context)

def manufacturer(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
    context = {
        "manufacturer": manufacturer,
    }
    return render(request, template_name="manufacturer.html", context=context)

def search(request):
    query = request.GET.get('query')
    manufacturers_search_results = Manufacturer.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(air_conditioners__technical_specifications__indoor_unit_dimensions__icontains=query) | Q(air_conditioners__technical_specifications__outdoor_unit_dimensions__icontains=query) | Q(air_conditioners__technical_specifications__energy_efficiency_class__icontains=query) | Q(air_conditioners__technical_specifications__operating_temperature__icontains=query) | Q(air_conditioners__technical_specifications__power__icontains=query) | Q(air_conditioners__technical_specifications__price__icontains=query) | Q(air_conditioners__country__name__icontains=query)).distinct()
    airconditioners_search_results = AirConditioner.objects.filter(Q(model_name__icontains=query) | Q(manufacturer__name__icontains=query) | Q(country__name__icontains=query) | Q(technical_specifications__indoor_unit_dimensions__icontains=query) | Q(technical_specifications__outdoor_unit_dimensions__icontains=query) | Q(technical_specifications__energy_efficiency_class__icontains=query) | Q(technical_specifications__operating_temperature__icontains=query) | Q(technical_specifications__power__icontains=query) | Q(technical_specifications__price__icontains=query)).distinct()
    technicalspecifications_search_results = TechnicalSpecification.objects.filter(Q(indoor_unit_dimensions__icontains=query) | Q(outdoor_unit_dimensions__icontains=query) | Q(energy_efficiency_class__icontains=query) | Q(operating_temperature__icontains=query) | Q(power__icontains=query) | Q(price__icontains=query) | Q(air_conditioner__manufacturer__name__icontains=query) | Q(air_conditioner__model_name__icontains=query) | Q(air_conditioner__country__name__icontains=query)).distinct()
    manufacturers_by_model_name = Manufacturer.objects.filter(air_conditioners__model_name__icontains=query).distinct()
    context = {
        "query": query,
        "manufacturers": (manufacturers_search_results | manufacturers_by_model_name).distinct(),
        "airconditioners": airconditioners_search_results,
        "technicalspecifications": technicalspecifications_search_results,
    }
    return render(request, template_name="search.html", context=context)

class AirConditionerListView(generic.ListView):
    model = AirConditioner
    context_object_name = 'airconditioners'
    template_name = 'airconditioners.html'
    paginate_by = 3

class AirConditionerDetailView(generic.DetailView):
    model = AirConditioner
    context_object_name = 'airconditioner'
    template_name = 'airconditioner.html'

class TechnicalSpecificationListView(ListView):
    model = TechnicalSpecification
    template_name = 'technicalspecifications.html'
    context_object_name = 'technicalspecifications'
    paginate_by = 3

class TechnicalSpecificationDetailView(DetailView):
    model = TechnicalSpecification
    template_name = 'technicalspecification.html'
    context_object_name = 'technicalspecification'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        print(obj.__dict__)  # išvesti objekto duomenis
        return obj

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    try:
                        password_validation.validate_password(password)
                    except password_validation.ValidationError as e:
                        for error in e:
                            messages.error(request, error)
                        return redirect('register')

                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')