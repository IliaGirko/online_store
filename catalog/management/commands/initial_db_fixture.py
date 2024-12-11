from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "load data from fixture"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Загрузка данными из фикстуры прошла успешно"))
