from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create default site and superuser'

    def handle(self, *args, **kwargs):
        site, created = Site.objects.get_or_create(
            domain="0.0.0.0:8002",
            defaults={'name': "0.0.0.0:8002"}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Site created: {site.domain}"))
        else:
            self.stdout.write(self.style.WARNING(f"Site already exists: {site.domain}"))

        User = get_user_model()
        
        if not User.objects.filter(email='admin@admin.com').exists():
            if User._meta.get_field('username'):
                User.objects.create_superuser(username='admin', email='admin@admin.com', password='admin')
                self.stdout.write(self.style.SUCCESS("Superuser 'admin' with username created"))
            else:
                User.objects.create_superuser(email='admin@admin.com', password='admin')
                self.stdout.write(self.style.SUCCESS("Superuser 'admin' without username created"))
