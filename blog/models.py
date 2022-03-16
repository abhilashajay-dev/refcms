from django.db import models
from wagtail.core.models import Page
from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.


class BlogListingPage(Page):
    template = 'blog/blog_listing_page.html'
    custom_title = models.CharField(max_length=255, blank=True, null=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        return context



    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
    ]    

class BlogDetailPage(Page):
    template = 'blog/blog_detail_page.html'
    custom_title = models.CharField(max_length=255, blank=False, null=False)
    blog_image = models.ForeignKey("wagtailimages.image", null=True, blank=False, on_delete=models.SET_NULL, related_name='+')

    content = StreamField([
        ("title_and_text", blocks.TitleAndTextBLock()),
        ("full_richtext", blocks.RichtextBlock()),
        ("simple_richtext", blocks.SimpleRichtextBlock()),
        ("cards", blocks.CardBlock()),
        ("cta", blocks.CTABlock()),
    ], null=True, blank=True )


    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        ImageChooserPanel('blog_image'),
        StreamFieldPanel('content'),

    ]