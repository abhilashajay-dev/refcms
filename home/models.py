from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    """ Home page model """

    templates = "home/home_page.html"
    max_count = 10

    banner_title = models.CharField(blank=False, max_length=50, null=True)
    banner_subtitle = RichTextField()
    banner_image = models.ForeignKey(
        'wagtailimages.image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    
    
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel('banner_subtitle'),
        PageChooserPanel('banner_cta'),
        ImageChooserPanel('banner_image'),

    ]

