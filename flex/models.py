from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from django.conf import settings

from streams import blocks

from wagtailcontentstream.models import ContentStreamPage, SectionContentStreamPage, ContentStreamPageWithRawCode

from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

# Create your models here.
class FlexPage(Page):
    template = 'flex/flex_page.html'

    subtitle = models.CharField(max_length=250, null=True, blank=True)
    content = StreamField([
        ("title_and_text", blocks.TitleAndTextBLock()),
        ("full_richtext", blocks.RichtextBlock()),
        ("simple_richtext", blocks.SimpleRichtextBlock()),
        ("cards", blocks.CardBlock()),
        ("cta", blocks.CTABlock()),
    ], null=True, blank=True )


    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),

    ]

    class Meta: 
        verbose_name = 'flex page'
        verbose_name_plural = 'flex pages'


class StandardPage(ContentStreamPage):
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL)

    content_panels = [
        FieldPanel('authors'),
    ] + ContentStreamPage.content_panels

class SectionStandardPage(SectionContentStreamPage):
    pass

class StandardPageWithRawCode(ContentStreamPageWithRawCode):
    pass


class BlockPage(Page):
    body = StreamField([
        ('header', HeaderBlock()),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
        ('map', MapBlock()),
        ('image_slider', ImageSliderBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="Full"),
    ]