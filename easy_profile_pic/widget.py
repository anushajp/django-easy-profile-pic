from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from . import client

class ProfilePicWidget(forms.widgets.Widget):

    def __init__(self, pic_src, profile_pic_container_class,
                 gtag_attrs={}, js_params={}, *args, **kwargs):

        super(ProfilePicWidget, self).__init__(*args, **kwargs)
        self.gtag_attrs = gtag_attrs
        self.js_params = js_params
        self.easy_pic_source = pic_src
        self.profile_pic_container_class = profile_pic_container_class

    def render(self, value, gtag_attrs=None, **kwargs):
        print(kwargs)
        return mark_safe(u'%s' % client.displayhtml(self.easy_pic_source,
                                                    self.profile_pic_container_class,
                                                    self.gtag_attrs,
                                                    self.js_params))