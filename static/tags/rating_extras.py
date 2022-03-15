from django import template

register = template.Library()

@register.filter(name='avg')
def avg(rating):
    total_score = rating.design + rating.usability + rating.content 
    return total_score // 3
