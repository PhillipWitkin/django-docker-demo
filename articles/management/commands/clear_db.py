from django.core.management.base import BaseCommand, CommandError
from articles.models import *
from django.core import management


class Command(BaseCommand):
    help = 'Meta command which calls other commands'

    def handle(self, *args, **options):
        print("Clearing previous entries...")
        Author.objects.all().delete()
        Article.objects.all().delete()
