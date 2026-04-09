from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ContentVersion

@receiver([post_save, post_delete], sender=ContentVersion)
def sync_content_loaders(sender, instance, **kwargs):
    content = instance.content

    loaders = set(
        v.loader for v in content.versions.all() if v.loader
    )

    content.loaders.set(loaders)