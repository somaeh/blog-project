from django.template import Library

register = Library()

@register.inclusion_tag('blog_app/result.html')
def show_result(queryset):
    return {'objects': queryset}