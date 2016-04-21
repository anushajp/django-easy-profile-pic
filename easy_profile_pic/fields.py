import os
import sys

from django import forms
from django.conf import settings

try:
    from django.utils.encoding import smart_unicode
except ImportError:
    from django.utils.encoding import smart_text as smart_unicode

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from . import client
from .widget import ProfilePicWidget


class ProfilePicField(forms.ImageField):
    # default_error_messages = {
    #     'captcha_invalid': _('Incorrect, please try again.')
    # }

    def __init__(self, pic_width='20px', pic_height='20px',
                 pic_class='django_profile_pic',
                 gtag_attrs={}, js_params={}, *args, **kwargs):
        """
        site_key = the Google provided site_key
        secret_key = the Google provided secret_key
        gtag_attrs = html input attributes to provide
            to the g-recaptcha tag
        js_params = parameters to passed to the javascript backend
        See: https://developers.google.com/recaptcha/docs/display
        """
        pic_width = pic_width if pic_width else \
            settings.PROFILE_PIC_WIDTH
        pic_height = pic_height if pic_height else \
            settings.PROFILE_PIC_HEIGHT
        pic_class = pic_class if pic_class else \
            settings.PROFILE_PIC_CLASS

        self.widget = ProfilePicWidget(
            pic_width=pic_width, pic_height=pic_height, pic_class=pic_class,
            gtag_attrs=gtag_attrs, js_params=js_params)
        self.required = True
        super(ProfilePicField, self).__init__(*args, **kwargs)

    def clean(self, value):
        super(ProfilePicField, self).clean(value)
        return value

