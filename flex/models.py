from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

from streams import blocks

# Create your models here.
class FlexPage(Page):
    template = 'flex/flex_page.html'

    subtitle = models.CharField(max_length=250, null=True, blank=True)
    content = StreamField([
        ("title_and_text", blocks.TitleAndTextBLock()),
    ], null=True, blank=True )


    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),

    ]

    class Meta: 
        verbose_name = 'flex page'
        verbose_name_plural = 'flex pages'