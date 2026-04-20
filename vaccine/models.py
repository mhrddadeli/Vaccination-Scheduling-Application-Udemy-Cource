from django.db import models


class Vaccine(models.Model):
    name = models.CharField("Vaccine Name", max_length=255)
    description = models.TextField(max_length=1024)
    number_doses = models.IntegerField(default=1)
    interval = models.IntegerField(default=0, help_text="Please provide interval in days.")
    storage_temperature = models.IntegerField(null=True, blank=True,
                                              help_text="Please provide storage temperature in Celsius.")
    minimum_age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
