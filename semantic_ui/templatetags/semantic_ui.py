from django import template
from django.template import loader, Context


register = template.Library()



@register.simple_tag
def semantic_header(
            content,
            icon=None,
            inverted=False,
            divider=False,
        ):
    """
    A simple tag that outputs a semantic ui header.

    Options are:

    * icon[None]: use semantic ui icon class ;
    * inverted[False]: to invert the header
    * divider[False]: for a centered dividing header
    """
    template = loader.get_template('semantic-ui/header.html')
    return template.render(Context({
        'content': content,
        'icon': icon,
        'inverted': inverted,
        'divider': divider,
    }))


@register.simple_tag
def semantic_icon(icon):
    return '<i class="{icon} icon"></i>'.format(
        icon=icon,
    )
