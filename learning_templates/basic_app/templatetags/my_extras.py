from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """

    WTF
    """
    return value.replace(arg,'')

# register.filter('cut',cut)