""" Stream fields live in here"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBLock(blocks.StructBlock):
    """Title and Text and nothing Else"""
    title =  blocks.CharBlock(required=True,
    help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add your additional text')

    class Meta:
        template = 'streams/title_and_text.html'
        icon = 'edit'
        label = 'Title & Text'


class RichtextBlock(blocks.RichTextBlock):
    """Rich Text Block with all the features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Rich Text Block without all features"""
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = ["bold","italic","link"]

  

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"



class CardBlock(blocks.StructBlock):
    """Cards for Home Page"""
    title = blocks.CharBlock(required=False, help_text='Add your title', blank=True, null=True)
    cards = blocks.ListBlock(blocks.StructBlock([   # ListBlock
        ('image', ImageChooserBlock(required=True)),
        ('title', blocks.CharBlock(required=True, max_length=250)),
        ('text', blocks.TextBlock(required=True, max_length=250)),
    ]))

    class Meta:
        template = "streams/card.html"
        icon = "placeholder"
        label = "Fake image slider"


class CTABlock(blocks.StructBlock):
    """Cta for Home Page"""
    title = blocks.CharBlock(required=False, help_text='Add your title', blank=True, null=True)
    text = blocks.TextBlock(required=True, max_length=250)
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn more', max_length=255) #external link 

    class Meta:
        template = "streams/cta.html"
        icon = "placeholder"
        label = "Call to Action"