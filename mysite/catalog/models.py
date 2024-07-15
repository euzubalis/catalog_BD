from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(verbose_name="Šalis", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Šalis"
        verbose_name_plural = "Šalys"

class Manufacturer(models.Model):
    name = models.CharField(verbose_name="Gamintojas", max_length=100)
    description = models.TextField(verbose_name="Aprašymas", max_length=5000, default="")
    cover = models.ImageField(verbose_name="Logotipas", upload_to='covers', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gamintojas"
        verbose_name_plural = "Gamintojai"

class AirConditioner(models.Model):
    model_name = models.CharField(verbose_name="Modelis", max_length=100)
    description = models.TextField(verbose_name="Aprašymas", max_length=5000, default="")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='air_conditioners', verbose_name="Gamintojas")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='air_conditioners', verbose_name="Šalis")
    cover = models.ImageField(verbose_name="Nuotrauka", upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f'{self.manufacturer} - {self.model_name}'

    class Meta:
        verbose_name = "Oro Kondicionierius"
        verbose_name_plural = "Oro Kondicionieriai"

class TechnicalSpecification(models.Model):
    air_conditioner = models.ForeignKey(AirConditioner, on_delete=models.CASCADE, related_name='technical_specifications', verbose_name="Oro kondicionierius")
    indoor_unit_dimensions = models.CharField(verbose_name="Vidinio bloko matmenys", max_length=50)
    outdoor_unit_dimensions = models.CharField(verbose_name="Išorinio bloko matmenys", max_length=50)
    energy_efficiency_class = models.CharField(verbose_name="Energijos efektyvumo klasė", max_length=10)
    operating_temperature = models.CharField(verbose_name="Darbinės temperatūros ribos šaldymas/šildymas", max_length=50)
    outdoor_unit_weight = models.DecimalField(verbose_name="Svoris išorinio bloko (kg)", max_digits=10, decimal_places=2)
    indoor_unit_weight = models.DecimalField(verbose_name="Svoris vidinio bloko (kg)", max_digits=10, decimal_places=2)
    power = models.DecimalField(verbose_name="Galingumas (kW)", max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(verbose_name="Kaina", max_digits=10, decimal_places=2, default=0)
    cover = models.ImageField(verbose_name="Nuotrauka", upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"Technininė specifikacija: {self.air_conditioner} {self.power} kW"

    class Meta:
        verbose_name = "Techninė specifikaciją"
        verbose_name_plural = "Techninės specifikacijos"

class ConditionerOrder(models.Model):
    air_conditioner = models.ForeignKey(to="TechnicalSpecification", verbose_name="Techninė specifikacija", on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    client = models.ForeignKey(to=User, verbose_name="Klientas", on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Užsakymas", max_length=5000)

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"
        ordering = ["-date_created"]

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Nuotrauka", default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"