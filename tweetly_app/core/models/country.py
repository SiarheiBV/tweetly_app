from django.db import models


class CountryModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "country"
