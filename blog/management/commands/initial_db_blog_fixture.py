from django.core.management import call_command
from django.core.management.base import BaseCommand

from blog.models import Post


class Command(BaseCommand):
    help = "load data from fixture"

    def handle(self, *args, **options):
        Post.objects.all().delete()
        call_command("loaddata", "blog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Загрузка данными из фикстуры прошла успешно"))
