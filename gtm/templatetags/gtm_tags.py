from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag("gtm/gtm.html")
def gtm(google_tag_id=None):
    if google_tag_id is None:
        google_tag_id = getattr(settings, 'GOOGLE_TAG_ID', None);
    return {
        'google_tag_id': google_tag_id
    }

@register.inclusion_tag("gtm/gtm_body.html")
def gtm_head(google_tag_id=None):
    if google_tag_id is None:
        google_tag_id = getattr(settings, 'GOOGLE_TAG_ID', None);
    return {
        'google_tag_id': google_tag_id
    }

@register.inclusion_tag("gtm/gtm_head.html")
def gtm_body(google_tag_id=None):
    if google_tag_id is None:
        google_tag_id = getattr(settings, 'GOOGLE_TAG_ID', None);
    return {
        'google_tag_id': google_tag_id
    }
