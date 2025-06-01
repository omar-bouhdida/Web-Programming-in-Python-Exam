from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
import re
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import regenerate_static_page


class PageContent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    content_type = models.CharField(max_length=50, default='article')
    meta_description = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='content', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Validate slug format
        if self.slug:
            if not re.match(r'^[a-z0-9-]+$', self.slug):
                raise ValidationError({'slug': 'Slug must be lowercase, alphanumeric, and hyphenated only.'})

        # Publish date logic
        if self.is_published and not self.publish_date:
            # Auto-set publish date to now if content is published but no date is set
            self.publish_date = timezone.now()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while PageContent.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug

        self.full_clean()  # Run model validations
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
@receiver(post_save, sender=PageContent)
def trigger_page_regeneration(sender, instance, **kwargs):
    if instance.is_published:
        regenerate_static_page.delay(instance.slug)