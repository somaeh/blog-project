from django import template
import datetime


register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)    #زمان فعلی سیستم را نمایش می دهد 
# @register.simple_tag
# def current_time(formate_string):
#     return datetime.datetime.now().strftime(formate_string)


@register.filter
def cutter(value, arg):
    return value[:arg]





