from django.conf import settings
from django.template import Library

register = Library()


def gtm_tag(google_tag_id=None):
    if google_tag_id is None:
        google_tag_id = getattr(settings, 'GOOGLE_TAG_ID', None)
    return {
        'google_tag_id': google_tag_id
    }


register.inclusion_tag("gtm/gtm.html", name='gtm')(gtm_tag)
register.inclusion_tag("gtm/gtm_head.html", name='gtm_head')(gtm_tag)
register.inclusion_tag("gtm/gtm_body.html", name='gtm_body')(gtm_tag)
