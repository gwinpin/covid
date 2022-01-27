from django.db.models import Count, Q
from datetime import datetime
from django.shortcuts import render
from .models import SickVaccine


def sick(request):
    # dataset = SickVaccine.objects.values('pozitivni_celkem', 'datum') \
    #     .annotate(survived_count=Count('pozitivni_celkem', filter=Q(survived=True)),
    #               not_survived_count=Count('pozitivni_celkem', filter=Q(survived=False))) \
    #     .order_by('datum')
    dataset = SickVaccine.objects.values().order_by('datum')
    date = datetime(2022, 1, 1)
    dataset2 = SickVaccine.objects.filter(datum__gt=date).values().order_by('datum')
    return render(request, 'vacine.html', {'dataset': dataset, 'dataset2': dataset2})


def sick2022(request):
    # dataset = SickVaccine.objects.values('pozitivni_celkem', 'datum') \
    #     .annotate(survived_count=Count('pozitivni_celkem', filter=Q(survived=True)),
    #               not_survived_count=Count('pozitivni_celkem', filter=Q(survived=False))) \
    #     .order_by('datum')
    date = datetime(2022, 1, 1)
    dataset = SickVaccine.objects.filter(datum__gt=date).values().order_by('datum')
    return render(request, 'vacine.html', {'dataset2': dataset})
