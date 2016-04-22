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


class ProfilePicField(forms.CharField):

    def __init__(self, gtag_attrs={}, js_params={},
                 *args, **kwargs):
        """
        site_key = the Google provided site_key
        secret_key = the Google provided secret_key
        gtag_attrs = html input attributes to provide
        js_params = parameters to passed to the javascript backend
        """
        self.custom_class = kwargs.pop('custom_class', None)
        print(kwargs)
        print (self.custom_class)
        if not kwargs:
            easy_pic_source = "https://spectroscopy.kaust.edu.sa/PublishingImages/icon_profile_unknown_300x300.png"
        else:
            if kwargs['initial']:
                easy_pic_source = kwargs['initial']
            else:
                easy_pic_source = "https://spectroscopy.kaust.edu.sa/PublishingImages/icon_profile_unknown_300x300.png"
        if self.custom_class:
            profile_pic_container_class = self.custom_class
        else:
            profile_pic_container_class = "easy-profile-pic-preview-container"

        self.widget = ProfilePicWidget(
            pic_src=easy_pic_source,profile_pic_container_class=profile_pic_container_class,
            gtag_attrs=gtag_attrs, js_params=js_params)
        self.required = True
        super(ProfilePicField, self).__init__(*args, **kwargs)

    # def widget_attrs(self, widget):
    #     attrs = super(ProfilePicField, self).widget_attrs(widget)
    #     if self.custom_class is not None:
    #         # The HTML attribute is maxlength, not max_length.
    #         attrs.update({'custom_class': str(self.cutom_class)})
    #     return attrs


    def clean(self, value):
        super(ProfilePicField, self).clean(value)
        return value

