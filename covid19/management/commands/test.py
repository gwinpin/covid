from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Обновление курсов валют, добавление новой валюты'

    def add_arguments(self, parser):
        parser.add_argument('-create', dest='create', action='store_true', help='create data')
        # parser.add_argument('-get', dest='get', action='store_true', help='get data')
        parser.add_argument('-name', dest='name', help='param name')
        parser.add_argument('-crypt', dest='crypt', help='crypt data')

    def handle(self, *args, **options):
        name = options.get('name')
        data = options.get('crypt')
        all = ContentType.objects.all()[0]
        a = 1
        # if options.get('create'):
        #     cr_set, created = CRSetting.objects.get_or_create(name=name)
        #     cr_data = pass_gen(data)
        #     if created:
        #         cr_set.value, cr_set._conf = cr_data
        #         cr_set.save()
        #         self.stdout.write(self.style.SUCCESS('Successfully create "%s"' % name))
        #     else:
        #         cr_set.value, cr_set._conf = cr_data
        #         cr_set.save()
        #         self.stdout.write(self.style.SUCCESS('Successfully update "%s"' % name))
        #
        # else:
        #     if CRSetting.objects.filter(name=name).exists():
        #         cr_s = CRSetting.objects.get(name=name)
        #         print(pass_get((bytes(cr_s.value), bytes(cr_s._conf))))

        self.stdout.write('Complete')
