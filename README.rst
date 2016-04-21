=====
Django Easy Profile Pic
=====

Easy Profile Pic is a simple Django app to customize the Profile image related things.

Quick start
-----------

1. Add "easy-profile-pic" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'easy-profile-pic',
    ]

2. Include the ProfilePicField to your forms.py like this::
    .....
    Picture = ProfilePicField()

3. Run your application