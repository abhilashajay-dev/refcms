from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks

from modelcluster.fields import ParentalKey



class HomePageCarouselImages(Orderable):
    """"Between 1 and 5 images for the home page carousel"""

    page = ParentalKey('home.HomePage', related_name='carousel_images')
    carousel_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=False
    )
    
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('carousel_image'),
        FieldPanel('caption'),
    ]




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

    content = StreamField([
        ('cta', blocks.CTABlock()),
    ], null=True, blank=True)    
    
    
    content_panels = Page.content_panels + [
   
        MultiFieldPanel([

        FieldPanel("banner_title"),
        FieldPanel('banner_subtitle'),
        PageChooserPanel('banner_cta'),
        ImageChooserPanel('banner_image'),
        StreamFieldPanel('content'),

        ], heading="Banner Options"),
        MultiFieldPanel([ InlinePanel('carousel_images', label="Carousel Images"), ], heading='Carousel Images')
    ]

