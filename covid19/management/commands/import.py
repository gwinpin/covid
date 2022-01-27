from django.core.management.base import BaseCommand
import pandas as pd
import requests
from covid19.models import SickVaccine


def check_column(model, df):
    column_name = []
    for c_name in df.columns:
        if c_name != 'id' and c_name in [f.name for f in model._meta.fields] + \
                [f'{f.name}_id' for f in model._meta.fields]:
            column_name.append(c_name)
    return column_name


def get_feed(address, file_name):
    r = requests.get(address, allow_redirects=True)
    if r.ok:
        open(f'{file_name}', 'wb').write(r.content)


class Command(BaseCommand):
    help = 'Обновление курсов валют, добавление новой валюты'

    def add_arguments(self, parser):
        parser.add_argument('-lang', dest='lang', help='source name')

    def handle(self, *args, **options):
        lang = options.get('lang')
        address = 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/osoby.csv'
        # get_feed(address, 'osoby.csv')
        file_name = 'ockovani-pozitivni.csv'
        address = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/ockovani-pozitivni.csv"
        get_feed(address, file_name)
        df = pd.read_csv(file_name)
        column_name = check_column(SickVaccine, df)
        obj = (SickVaccine(**vols) for vols in df[column_name].to_dict('records'))
        SickVaccine.objects.bulk_create(obj)
        self.stdout.write('Complete')
