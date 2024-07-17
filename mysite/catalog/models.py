from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import gettext_lazy as _

class Country(models.Model):
    name = models.CharField(verbose_name=_("Country"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

class Manufacturer(models.Model):
    name = models.CharField(verbose_name=_("Manufacturer"), max_length=100)
    description = models.TextField(verbose_name=_("Description"), max_length=5000, default="")
    cover = models.ImageField(verbose_name=_("Logo"), upload_to='covers', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")

class AirConditioner(models.Model):
    model_name = models.CharField(verbose_name=_("Model"), max_length=100)
    description = models.TextField(verbose_name=_("Description"), max_length=5000, default="")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='air_conditioners', verbose_name=_("Manufacturer"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='air_conditioners', verbose_name=_("Country"))
    cover = models.ImageField(verbose_name=_("Photo"), upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f'{self.manufacturer} - {self.model_name}'

    class Meta:
        verbose_name = _("Air Conditioner")
        verbose_name_plural = _("Air Conditioners")

class TechnicalSpecification(models.Model):
    air_conditioner = models.ForeignKey(AirConditioner, on_delete=models.CASCADE, related_name='technical_specifications', verbose_name=_("Air Conditioner"))
    indoor_unit_dimensions = models.CharField(verbose_name=_("Indoor unit dimensions"), max_length=50)
    outdoor_unit_dimensions = models.CharField(verbose_name=_("Outdoor unit dimensions"), max_length=50)
    energy_efficiency_class = models.CharField(verbose_name=_("Energy efficiency class"), max_length=10)
    operating_temperature = models.CharField(verbose_name=_("Operating temperature"), max_length=50)
    outdoor_unit_weight = models.DecimalField(verbose_name=_("Outdoor unit weight (kg)"), max_digits=10, decimal_places=2)
    indoor_unit_weight = models.DecimalField(verbose_name=_("Indoor unit weight (kg)"), max_digits=10, decimal_places=2)
    power = models.DecimalField(verbose_name=_("Power (kW)"), max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2, default=0)
    cover = models.ImageField(verbose_name=_("Cover"), upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"Technininė specifikacija: {self.air_conditioner} {self.power} kW"

    class Meta:
        verbose_name = _("Technical Specification")
        verbose_name_plural = _("Technical Specifications")

class ConditionerOrder(models.Model):
    air_conditioner = models.ForeignKey(to="TechnicalSpecification", verbose_name=_("Technical specification"), on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    client = models.ForeignKey(to=User, verbose_name=_("Client"), on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    content = models.TextField(verbose_name=_("Order"), max_length=5000)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ["-date_created"]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.photo.path)
