from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    Retrieves all lettings from the database and passes them to the template for rendering
    Args:
        request: HttpRequest object representing the request made to the server.

    Returns:
        HttpResponse: Response object containing the rendered index page.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Retrieves the letting with the specified ID from the database and passes its details
    to the template for rendering.
    Args:
        request: HttpRequest object representing the request made to the server.
        letting_id: The ID of the letting to retrieve details for.

    Returns:
        HttpResponse: Response object containing the rendered letting details page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
