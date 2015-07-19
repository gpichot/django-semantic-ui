from django import template
from django.template import loader, Context


register = template.Library()



@register.simple_tag
def semantic_header(
            content,
            icon=None,
            inverted=False,
            divider=False,
            level=1,
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
        'level': level,
    }))


@register.simple_tag
def semantic_icon(icon, klass=''):
    return '<i class="{icon} icon"></i>'.format(
        icon=icon,
    )


@register.simple_tag
def semantic_button(content, icon=None, klass=None):
    template = loader.get_template('semantic-ui/button.html')
    return template.render(Context({
        'content': content,
        'icon': icon,
        'class': klass,
    }))


@register.simple_tag
def semantic_button_link(url, content='', icon=None, klass=None, as_popup=True):
    template = loader.get_template('semantic-ui/button_link.html')
    return template.render(Context({
        'url': url,
        'content': content,
        'icon': icon,
        'class': klass,
        'as_popup': True,
    }))
