django-google-tag-manager
=========================

Template tag to install your Google Tag Manager account in your
templates (http://www.google.com/tagmanager/)

## Installation and Usage

1. run `pip install django-google-tag-manager`
2. add `'gtm'` to your `INSTALLED_APPS` setting.
3. set `GOOGLE_TAG_ID` to your Google Tag Container Id. It
   should look something like `GTM_XXXXXX`
4. In your templates (probably in your base template) you `{% load
   gtm_tags %}` and then `{% gtm %}` just below your `<body>` opening tag.
5. Profit

That's it for the most part. If for any reason you want to override
the template used to render the tag, it's called `gtm/gtm.html`.

Optionally, you can pass the google tag id as a parameter to the
templatetag like this:

    {% gtm "GTM-ABC123" %}

