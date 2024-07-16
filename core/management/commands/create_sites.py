from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Creates sites'
    user = {}

    def add_arguments(self, parser):
        parser.add_argument('sites', type=str, help='domain')

    def handle(self, *args, **options):
        try:
            Site.objects.create(name=options['sites'], domain=options['sites'])
            self.stdout.write(self.style.SUCCESS('Сайт добавлен'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Сайт добавлен'))
