import logging

import django

if django.VERSION[1] >= 5:
    import json
else:
    from django.utils import simplejson as json

from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import get_language
# from django.utils.encoding import force_text

# from ._compat import want_bytes, urlencode, Request, urlopen, PY2

logger = logging.getLogger(__name__)
DEFAULT_WIDGET_TEMPLATE = 'widget.html'
WIDGET_TEMPLATE = getattr(settings, "NORECAPTCHA_WIDGET_TEMPLATE",
                          DEFAULT_WIDGET_TEMPLATE)

def displayhtml(gtag_attrs, js_params):
    """Gets the HTML to display for reCAPTCHA
    site_key -- The public api key provided by Google ReCaptcha
    """

    if 'hl' not in js_params:
        js_params['hl'] = get_language()[:2]

    return render_to_string(
        WIDGET_TEMPLATE,
        {
            'anusha': 'anusha1',
            'js_params': js_params,
            'gtag_attrs': gtag_attrs,
        })