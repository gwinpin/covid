import uuid
from django.db import models
from datetime import datetime


class SickVaccine(models.Model):

    datum = models.DateField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pozitivni_celkem = models.IntegerField(null=True, blank=True)
    pozitivni_bez_ockovani = models.IntegerField(null=True, blank=True)
    pozitivni_nedokoncene_ockovani = models.IntegerField(null=True, blank=True)
    pozitivni_dokoncene_ockovani = models.IntegerField(null=True, blank=True)
    pozitivni_posilujici_davka = models.IntegerField(null=True, blank=True)
