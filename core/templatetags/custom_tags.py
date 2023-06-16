from core.models import News,Appointment
from django import template
register=template.Library()
@register.simple_tag
def get_news(order,offset,limit):
    if order==0:
        return News.objects.filter(is_active=True).order_by('-updated_at')[offset:limit]
    else:
        return News.objects.filter(is_active=True).order_by('created_at')[offset:limit]

