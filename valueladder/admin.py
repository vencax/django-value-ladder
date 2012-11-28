from django.contrib import admin
from feincms.translations import admin_translationinline

from .models import Thing, ThingValue
from valueladder.models import ThingTranslation

ThingTranslationInline = admin_translationinline(ThingTranslation,
    prepopulated_fields={'slug': ('title',)})


class ThingAdmin(admin.ModelAdmin):
    inlines = [ThingTranslationInline]
    list_display = ['__unicode__', 'code']
    search_fields = ['translations__title', 'code']


class ThingValueAdmin(admin.ModelAdmin):
    search_fields = ['thingA', 'thingB']
    list_display = ['thingA', 'thingB', 'ratio']

admin.site.register(Thing, ThingAdmin)
admin.site.register(ThingValue, ThingValueAdmin)
