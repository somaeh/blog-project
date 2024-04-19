from django import template
import datetime



register = template.Library()
# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

# @register.simple_tag
# def time(format_string):
#     return datetime.datetime.now().strftime(format_string)
@register.simple_tag()
def time_now(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.filter()
def cut(value, arg):
    
    return value[:arg]




def cuter(value, arg):
    return value[:arg]

register.filter(cuter)

