from django.db import models
from django.utils.translation import gettext_lazy as _
from feincms import translations
from django.template.defaultfilters import slugify

class Thing(models.Model, translations.TranslatedObjectMixin):
    """
    Represents a thing ... :)
    """
    code = models.CharField(_('code'), max_length=16)
    
    objects = translations.TranslatedObjectManager()

class ThingTranslation(translations.Translation(Thing)):
    title = models.CharField(_('category title'), max_length=32)
    slug = models.SlugField(_('slug'), unique=True)
    description = models.CharField(_('description'), max_length=256, blank=True)

    class Meta:
        verbose_name = _('thing translation')
        verbose_name_plural = _('thing translations')
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('forum_category', (), {
            'slug': self.slug,
            })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:32]

        super(ThingTranslation, self).save(*args, **kwargs)

class ThingValue(models.Model):
    """
    Value ratio between the two things.
    """
    class Meta:
        unique_together = ('thingA', 'thingB', 'ratio')

    thingA = models.ForeignKey(Thing, related_name='changing_things')
    thingB = models.ForeignKey(Thing, related_name='changed_things')
    ratio = models.FloatField(_('value ratio between the 2'))