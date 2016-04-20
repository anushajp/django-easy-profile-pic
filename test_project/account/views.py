from django.shortcuts import render

from account.forms import ProfileForm


def profile(request):
    """
    This method redirects the user to the profile page.
    """
    form = ProfileForm
    return render(request, 'profile.html', locals())
