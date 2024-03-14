from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """
    Retrieves all profiles from the database and passes them to the template for rendering
    Args:
        request: HttpRequest object representing the request made to the server.

    Returns:
        HttpResponse: Response object containing the rendered index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Retrieves the profile with the specified username from the database and passes its details
    to the template for rendering
    Args:
        request: HttpRequest object representing the request made to the server.
        username: The username of the profile to retrieve details for.

    Returns:
        HttpResponse: Response object containing the rendered profile details page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
