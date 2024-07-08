from django.db import models

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

    def __str__(self):
        return f"Technical specs for {self.air_conditioner}"

    class Meta:
        verbose_name = "Techninė specifikaciją"
        verbose_name_plural = "Techninės specifikacijos"




