from django.shortcuts import render


def index(request):
    """
    Renders the index.html template.
    Args:
        request: HttpRequest object representing the request made to the server

    Returns:
        HttpResponse: Response object containing the rendered index page
    """
    return render(request, 'index.html')


def handler404(request, exception):
    """
    Renders the 404.html template with a 404 status code
    Args:
        request: HttpRequest object representing the request made to the server.
        exception: Exception object representing the exception that triggered the 404 error

    Returns:
        HttpResponse: Response object containing the rendered 404 error page with a 404 status code
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Renders the 500.html template with a 500 status code
    Args:
        request: HttpRequest object representing the request made to the server

    Returns:
        HttpResponse: Response object containing the rendered 500 error page with a 500 status code
    """
    return render(request, '500.html', status=500)
