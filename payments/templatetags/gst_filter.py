from django import template
register = template.Library()

@register.filter
def calc_gst(value):
    try:
        value = int(value)
        gst_rate = 0.18
        if value: 
            return (value - (value*gst_rate))
    except: 
        pass
    return ''