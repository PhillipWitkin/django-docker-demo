from django.core.management.base import BaseCommand, CommandError
from articles.models import *
from django.core import management


class Command(BaseCommand):
    help = 'Meta command which calls other commands'

    def handle(self, *args, **options):
        print("Seeding Database...")
        querySetArticles = Article.objects.all()
        querySetAuthors = Author.objects.all()
        if querySetAuthors.count() == 0 and querySetArticles.count() == 0:
            print("Loading from seed_data.json...")
            management.call_command('loaddata', 'seed_data.json')
        else:
            print("Database has already been seeded")