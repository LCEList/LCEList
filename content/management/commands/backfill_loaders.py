from django.core.management.base import BaseCommand
from content.models import Content

class Command(BaseCommand):
    help = "Backfill content loaders from versions"

    def handle(self, *args, **kwargs):
        contents = Content.objects.prefetch_related('versions__loader')

        for content in contents:
            loaders = set(
                v.loader for v in content.versions.all() if v.loader
            )
            content.loaders.set(loaders)

        self.stdout.write(self.style.SUCCESS("Backfill complete"))