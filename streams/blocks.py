""" Stream fields live in here"""
from wagtail.core import blocks

class TitleAndTextBLock(blocks.StructBlock):
    """Title and Text and nothing Else"""
    title =  blocks.CharBlock(required=True,
    help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add your additional text')

    class Meta:
        template = 'streams/title_and_text.html'
        icon = 'edit'
        label = 'Title & Text'